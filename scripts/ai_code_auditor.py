#!/usr/bin/env -S uv run python
"""
scripts/ai_code_auditor.py - Automated Static Analysis, Pytest, & LLM Code Review
Target: Local Development Machine connecting to Desktop Ollama
Optimized for cross-platform (Linux/Windows) portability and high-concurrency AI review.
"""

import argparse
import os
import re
import sys
import subprocess
import requests
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Set
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console

# ==========================================
# CONFIGURATION & ENVIRONMENT SETUP
# ==========================================
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://192.168.1.90:11434/api/chat")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "hf.co/BugTraceAI/BugTraceAI-CORE-Pro:latest")

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PROJECT_DIR = Path(os.getenv("UNIFI_DIRECTOR_BASE", SCRIPT_DIR.parent)).resolve()
TARGET_DIR = Path(os.getenv("AUDIT_TARGET_DIR", BASE_PROJECT_DIR / "src/unifi_director")).resolve()
TEST_DIR = Path(os.getenv("AUDIT_TEST_DIR", BASE_PROJECT_DIR / "tests")).resolve()

# WHY: timestamp per-run so successive audit reports accumulate rather than
#      overwriting each other — matches the build_monolith.py convention.
_RUN_TS = datetime.now().strftime("%Y%m%d_%H%M%S")
REPORTS_DIR = BASE_PROJECT_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_REPORT = Path(
    os.getenv("AUDIT_OUTPUT_FILE", str(REPORTS_DIR / f"code_audit_report-{_RUN_TS}.md"))
).resolve()

console = Console()

class AuditEngine:
    def __init__(self):
        self.dependency_map: Dict[str, Set[str]] = {}
        self.console = console
        self.main_code = self._load_file(TARGET_DIR / "main.py")
        self.registry_code = self._load_file(TARGET_DIR / "registry.py")

    def map_dependencies(self, target_dir: Path) -> Dict[str, Set[str]]:
        """
        Maps Python imports to their respective files for dependency tracking.
        """

        dependencies: Dict[str, Set[str]] = {}
        for path in target_dir.rglob("*.py"):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            for match in re.finditer(r"^from\s+([\w.]+)\s+import", content, flags=re.MULTILINE):
                module_path = match.group(1)
                dependencies.setdefault(module_path, set()).add(
                    path.relative_to(target_dir).as_posix()
                )
            for match in re.finditer(r"^import\s+([\w.]+)", content, flags=re.MULTILINE):
                module_path = match.group(1)
                dependencies.setdefault(module_path, set()).add(
                    path.relative_to(target_dir).as_posix()
                )

        return dependencies

    def _load_file(self, path: Path) -> str:
        try:
            return path.read_text("utf-8")
        except FileNotFoundError:
            self.console.print(f"[red][!] Critical file missing: {path}[/red]")
            return ""

    def run_static_linter(self, target_dir: Path = TARGET_DIR) -> str:
        """
        Runs Ruff for strict PEP8/syntax and MyPy for Type Checking on a given directory.
        """

        self.console.print("[*] Running strict static analysis (Ruff/MyPy)...", style="bold blue")
        report = ""

        # 1. Ruff (PEP8 and Syntax)
        try:
            ruff_res = subprocess.run(
                [sys.executable, "-m", "ruff", "check", str(target_dir)],
                capture_output=True, text=True
            )
            if ruff_res.returncode == 0:
                self.console.print("[+] Ruff found zero PEP8 or syntax errors!", style="bold green")
                report += "### Ruff Static Analysis: PASS\nNo syntax or style violations found.\n\n"
            else:
                self.console.print("[-] Ruff found issues.", style="bold yellow")
                report += f"### Ruff Static Analysis: FAIL\n```text\n{ruff_res.stdout}\n```\n\n"
        except FileNotFoundError:
            report += "Ruff not installed. Run: `pip install ruff`\n\n"

        # 2. MyPy (Type Checking)
        try:
            mypy_res = subprocess.run(
                [sys.executable, "-m", "mypy", str(target_dir), "--ignore-missing-imports"],
                capture_output=True, text=True
            )
            if mypy_res.returncode == 0:
                self.console.print("[+] MyPy found zero type mismatches!", style="bold green")
                report += "### MyPy Type Checking: PASS\nAll function signatures match.\n\n"
            else:
                self.console.print("[-] MyPy found type issues.", style="bold yellow")
                report += f"### MyPy Type Checking: FAIL\n```text\n{mypy_res.stdout}\n```\n\n"
        except FileNotFoundError:
            report += "MyPy not installed. Run: `pip install mypy`\n\n"

        return report

    def run_pytest_suite(self, test_dir: Path = TEST_DIR) -> str:
        """
        Executes Pytest against the dedicated testing directory to verify functional integrity.
        """

        self.console.print("[*] Executing Pytest suite...", style="bold blue")
        report = ""

        try:
            pytest_res = subprocess.run(
                [sys.executable, "-m", "pytest", str(test_dir), "-q", "--tb=short"],
                capture_output=True,
                text=True
            )
            if pytest_res.returncode == 0:
                self.console.print("[+] Pytest suite passed successfully!", style="bold green")
                report += "### Pytest Execution: PASS\nAll unit tests passed successfully.\n\n"
            elif pytest_res.returncode == 5:
                self.console.print("[-] No tests found by Pytest.", style="bold yellow")
                report += "### Pytest Execution: NO TESTS FOUND\nEnsure your test files follow the `test_*.py` naming convention.\n\n"
            else:
                self.console.print("[-] Pytest suite failed.", style="bold red")
                report += f"### Pytest Execution: FAIL\n```text\n{pytest_res.stdout}\n```\n\n"
        except FileNotFoundError:
            report += "Pytest not installed. Run: `pip install pytest`\n\n"

        return report

    def ai_architectural_review(self, module_path: Path, module_code: str) -> str:
        """
        Feeds main.py, registry.py, and a target module to the LLM to verify the architectural contract.
        """

        self.console.print(f"[*] Verifying integration contract for: {module_path.name}...")

        system_prompt = (
            "You are a strict, conservative Software Architect. Review the integration between these three files. "
            f"The target module is `{module_path.name}`.\n\n"
            "ANTI-HALLUCINATION GUARDRAILS & RULES:\n"
            "1. Verify `main.py` accurately extracts configs from `registry.py` and passes them to the public functions of the target.\n"
            "2. DO NOT hallucinate missing parameters. Look strictly at the function signatures.\n"
            "3. If integration is correct, you MUST output exactly: 'Integration is optimal.'\n"
            "4. Output ONLY bullet points if genuine, code-breaking integration bugs are found."
        )

        user_prompt = (
            f"FILE 1: registry.py\n```python\n{self.registry_code}\n```\n\n"
            f"FILE 2: main.py\n```python\n{self.main_code}\n```\n\n"
            f"FILE 3: {module_path.name}\n```python\n{module_code}\n```"
        )

        payload = {
            "model": OLLAMA_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "stream": False,
            "options": {
                "temperature": 0.1,
                "num_ctx": 8192
            },
        }

        try:
            response = requests.post(OLLAMA_URL, json=payload, timeout=180)
            response.raise_for_status()
            return response.json().get("message", {}).get("content", "No response from model.")
        except Exception as e:
            return f"Ollama API Error during architectural review: {e}"

    def ai_code_review(self, file_path: Path, code_content: str) -> str:
        """
        Deep inspection for QoL, logic bugs, and Pi 5 hardware optimizations.
        """

        self.console.print(f"[*] Deep scanning {file_path.name} for optimizations...")

        system_prompt = (
            f"You are an elite, conservative Python performance engineer. Review `{file_path.name}`. "
            "This code runs on a Raspberry Pi 5 managing UniFi network infrastructure.\n\n"
            "CRITICAL ANTI-HALLUCINATION GUARDRAILS:\n"
            "1. DO NOT invent issues. If the code is structurally sound, you MUST output exactly: 'Code is optimal.'\n"
            "2. DO NOT suggest replacing `time.sleep()` or blocking calls with `asyncio`. Blocking calls are INTENTIONAL.\n"
            "3. DO NOT suggest `with open()` for file operations if the code ALREADY uses it.\n"
            "4. DO NOT suggest converting lists to generators if the script requires `len()` or multiple iterations.\n"
            "5. BEFORE suggesting a missing exception handler, ensure a `try/except` block doesn't already wrap it.\n"
            "6. DO NOT complain about PEP8, line lengths, or missing docstrings, unless it causes functional errors.\n"
            "7. DO NOT suggest replacing basic dicts with defaultdicts unless it significantly simplifies logic.\n\n"
            "FOCUS STRICTLY ON:\n"
            "- Memory leaks or unbounded growth.\n"
            "- Unhandled fatal exceptions that would crash the CLI mid-run.\n"
            "- API credential leaks (keys must never appear in logs or output).\n"
            "- Pi 5 constraints (excessive NVMe writes, blocking network calls without timeout)."
        )

        user_prompt = f"Code to review:\n```python\n{code_content}\n```"

        payload = {
            "model": OLLAMA_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "stream": False,
            "options": {
                "temperature": 0.1,
                "num_ctx": 8192
            },
        }

        try:
            response = requests.post(OLLAMA_URL, json=payload, timeout=120)
            response.raise_for_status()
            return response.json().get("message", {}).get("content", "No response from model.")
        except Exception as e:
            return f"Ollama API Error during code review: {e}"

    def run_sweep(self, deep_scan: bool = False):
        if not TARGET_DIR.exists():
            self.console.print(f"[!] Target directory {TARGET_DIR} not found!", style="bold red")
            return

        self.console.print("\n[bold green]Initiating UniFi Director 360° Codebase Sweep...[/bold green]\n")

        # 1. Static Linting & Testing Phase
        linter_results = self.run_static_linter()
        pytest_results = self.run_pytest_suite()

        # Collect modules to review (excluding core orchestration files)
        python_files = [
            f for f in TARGET_DIR.rglob("*.py")
            if f.name not in ["main.py", "registry.py", "__init__.py"]
        ]

        # 2. Parallel AI Review Execution
        ai_reviews: Dict[str, Any] = {}
        integration_reviews: Dict[str, Any] = {}

        with ThreadPoolExecutor(max_workers=2) as executor:
            for file in python_files:
                file_code = file.read_text("utf-8")

                if deep_scan:
                    ai_reviews[file.name] = executor.submit(self.ai_code_review, file, file_code)

                if deep_scan and any(part in file.parts for part in ["modules", "utils"]):
                    integration_reviews[file.name] = executor.submit(
                        self.ai_architectural_review, file, file_code
                    )

        # 3. Generate Markdown Report
        self.console.print(f"\n[*] Compiling final audit report to {OUTPUT_REPORT}...")
        with open(OUTPUT_REPORT, "w", encoding="utf-8") as f:
            f.write("# 🔴 UniFi Director — 360° Codebase Sweep Report\n\n")
            f.write(f"**Generated:** `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`\n\n")
            f.write("---\n\n")
            f.write("## 1. Static Analysis & Unit Tests\n")
            f.write(f"{linter_results}\n")
            f.write(f"{pytest_results}\n")

            f.write("## 2. Architectural Integration Tests\n")
            for filename, future in integration_reviews.items():
                self.console.print(f"[*] Finalizing contract check: {filename}")
                result = future.result()
                f.write(f"### Contract Check: `{filename}`\n")
                f.write(f"{result}\n\n")

            f.write("---\n## 3. Deep Dive & Footprint Optimizations\n")
            for filename, future in ai_reviews.items():
                self.console.print(f"[*] Finalizing deep dive: {filename}")
                result = future.result()
                f.write(f"### `{filename}`\n")
                f.write(f"{result}\n\n")

        self.console.print(f"[bold green][+] Sweep complete → {OUTPUT_REPORT.name}[/bold green]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UniFi Director — 360° Codebase Sweep")
    parser.add_argument("--deep-scan", action="store_true", help="Run per-file AI deep scan in addition to static analysis and integration checks")
    args = parser.parse_args()
    engine = AuditEngine()
    engine.run_sweep(deep_scan=args.deep_scan)
