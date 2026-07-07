import os
import ast
import re
import argparse
import logging
from pathlib import Path
from datetime import datetime
from typing import List, Set, Dict, TextIO

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# ==========================================
# CONFIGURATION & DEFAULTS
# ==========================================

DEFAULT_TARGET: Path = Path("/home/pi/UnifiDirector/src/unifi_director")
PROJECT_NAME: str = "Unifi Director"

VALID_EXTENSIONS: Set[str] = {'.py', '.sh', '.json', '.yaml', '.conf', '.txt', '.md', '.toml'}
IGNORE_DIRS: Set[str] = {'.git', '.venv', 'venv', '__pycache__', 'node_modules'}

# WHY: hoisted to module scope so it is built once, not rebuilt on every file
#      iteration inside the walk loop.
LANG_MAP: Dict[str, str] = {
    '.py': 'python',
    '.sh': 'bash',
    '.json': 'json',
    '.yaml': 'yaml',
    '.md': 'markdown',
}

# ==========================================

def default_output_name() -> Path:
    # WHY: computed at call time (not import time) so the timestamp reflects when
    #      the build actually runs, not when the module was first loaded.
    return Path(f"Project_Monolith-{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")

def stamp_output_path(path: Path) -> Path:
    """Inject a timestamp before the file extension of any output path."""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return path.with_stem(f"{path.stem}-{ts}")

def fence_for(content: str) -> str:
    """Return a backtick fence long enough to safely wrap `content`."""
    # WHY: a scanned file (especially .md) may itself contain ``` fences. If the
    #      outer fence is not longer than the longest backtick run inside, the
    #      inner run closes the block early and corrupts the whole monolith.
    longest_run: int = 0
    current_run: int = 0
    for char in content:
        if char == "`":
            current_run += 1
            longest_run = max(longest_run, current_run)
        else:
            current_run = 0
    return "`" * max(3, longest_run + 1)

def get_python_imports(filepath: Path) -> List[str]:
    """Parse a Python file with the AST to extract all imports."""
    imports: Set[str] = set()
    try:
        content: str = filepath.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(content, filename=str(filepath))

        # WHY: ast.walk visits every node, so imports nested inside functions,
        #      `if TYPE_CHECKING:` guards, and `try/except ImportError` fallback
        #      blocks are all captured — the full dependency surface, not just
        #      module-level declarations.
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module)
    except (SyntaxError, UnicodeDecodeError) as e:
        logger.warning("AST parsing error in %s: %s", filepath.name, e)
        return [f"AST Parsing Error: {e}"]
    except Exception as e:
        logger.error("Unexpected error parsing %s: %s", filepath.name, e)
        return [f"Unexpected Error: {e}"]

    return sorted(imports)

def write_monolith_header(outfile: TextIO, project_name: str) -> None:
    """Write the standardized header for the monolith file including a timestamp."""
    display_timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M")

    outfile.write(f"# 📚 {project_name} - Complete Source Code Monolith\n\n")
    outfile.write("This document contains the concatenated source code for the entire project.\n")
    outfile.write(f"**Generated on:** `{display_timestamp}`\n")
    outfile.write("Each file is separated by a metadata header indicating its original path and dependencies.\n\n")
    outfile.write("---\n\n")

def compile_monolith(target_dir: Path, output_path: Path) -> None:
    """Scan the target directory and concatenate valid files into a single Markdown monolith."""
    source_path: Path = target_dir.resolve()
    output_path = output_path.resolve()

    # WHY: is_dir() already returns False for a non-existent path, so the two
    #      original checks collapse into one.
    if not source_path.is_dir():
        logger.error("Target directory '%s' does not exist.", source_path)
        return

    if not os.access(output_path.parent, os.W_OK):
        logger.error("Permission denied: cannot write to %s", output_path)
        return

    logger.info("Scanning directory: %s", source_path)

    try:
        with open(output_path, "w", encoding="utf-8") as outfile:
            write_monolith_header(outfile, PROJECT_NAME)

            file_count: int = 0

            for root, dirs, files in os.walk(source_path):
                # WHY: prune ignored dirs AND sort in place so traversal order is
                #      deterministic — successive monoliths diff cleanly.
                dirs[:] = sorted(d for d in dirs if d not in IGNORE_DIRS)

                for file in sorted(files):
                    file_path: Path = Path(root) / file

                    # Skip the output file itself if it lives inside the scanned tree.
                    if file_path == output_path or file_path.name == output_path.name:
                        continue

                    if file_path.suffix not in VALID_EXTENSIONS:
                        continue

                    file_count += 1

                    # Relative path to reconstruct the directory structure.
                    rel_path: str = "/" + str(file_path.relative_to(source_path)).replace("\\", "/")

                    dependencies: List[str] = []
                    if file_path.suffix == '.py':
                        dependencies = get_python_imports(file_path)

                    try:
                        code_content: str = file_path.read_text(encoding="utf-8", errors="replace")
                    except Exception as e:
                        code_content = f"# [!] Error reading file content: {e}"
                        logger.warning("Failed to read content of %s: %s", file_path.name, e)

                    # -----------------------------------------
                    # WRITE THE METADATA HEADER
                    # -----------------------------------------
                    outfile.write(f"## FILE: `{rel_path}`\n\n")
                    outfile.write("```text\n")
                    outfile.write("====================================================================\n")
                    outfile.write(f"FILE_PATH: {rel_path}\n")

                    if dependencies:
                        outfile.write("DEPENDENCIES_IMPORTED:\n")
                        for dep in dependencies:
                            outfile.write(f"  - {dep}\n")
                    else:
                        outfile.write("DEPENDENCIES_IMPORTED: None\n")

                    outfile.write("====================================================================\n")
                    outfile.write("```\n\n")

                    # -----------------------------------------
                    # WRITE THE CODE BLOCK
                    # -----------------------------------------
                    lang: str = LANG_MAP.get(file_path.suffix, 'text')

                    # WHY: dynamic fence prevents inner ``` runs (common in .md
                    #      files) from prematurely closing this code block.
                    fence: str = fence_for(code_content)

                    outfile.write(f"{fence}{lang}\n")
                    outfile.write(code_content)
                    if not code_content.endswith("\n"):
                        outfile.write("\n")
                    outfile.write(f"{fence}\n\n")
                    outfile.write("---\n\n")

                    logger.debug("Added: %s", rel_path)

        logger.info("Success! %d files compiled into '%s'.", file_count, output_path)

    except PermissionError:
        logger.error("Permission denied writing to %s", output_path)
    except Exception as e:
        logger.critical("Fatal error during compilation: %s", e)

def recreate_from_monolith(monolith_path: Path, dest_dir: Path) -> None:
    """
    Parse a previously generated monolith and restore each embedded file to dest_dir,
    preserving the relative directory structure encoded in the ## FILE: headers.
    """
    # WHY: resolve() anchors dest_dir to an absolute path before any write so
    #      path-traversal sequences (e.g. `../../`) in FILE_PATH entries cannot
    #      escape the intended destination tree.
    dest_dir = dest_dir.resolve()

    if not monolith_path.is_file():
        logger.error("Monolith file not found: %s", monolith_path)
        return

    dest_dir.mkdir(parents=True, exist_ok=True)

    lines: List[str] = monolith_path.read_text(encoding="utf-8", errors="replace").splitlines()
    n: int = len(lines)
    file_count: int = 0
    i: int = 0

    while i < n:
        # ── Step 1: locate a ## FILE: section header ──────────────────────────
        header_match = re.match(r'^## FILE: `(.+?)`', lines[i])
        if not header_match:
            i += 1
            continue

        rel_path: str = header_match.group(1).lstrip("/")
        i += 1

        # ── Step 2: skip to the opening ```text metadata block ────────────────
        while i < n and not lines[i].startswith("```text"):
            i += 1
        if i >= n:
            break
        i += 1  # skip the ```text line itself

        # ── Step 3: skip to the closing ``` of the metadata block ─────────────
        while i < n and not re.match(r'^```\s*$', lines[i]):
            i += 1
        if i >= n:
            break
        i += 1  # skip the closing ``` line

        # ── Step 4: skip any blank lines between metadata and code fence ───────
        while i < n and not lines[i].strip():
            i += 1
        if i >= n:
            break

        # ── Step 5: parse the dynamic opening code fence ──────────────────────
        fence_match = re.match(r'^(`{3,})', lines[i])
        if not fence_match:
            # Not a fenced block — unexpected format, skip this section.
            logger.warning("Expected code fence after metadata for '%s'; skipping.", rel_path)
            i += 1
            continue
        code_fence: str = fence_match.group(1)
        i += 1  # skip the fence + lang identifier line

        # ── Step 6: collect code lines until the matching close fence ──────────
        code_lines: List[str] = []
        while i < n and lines[i] != code_fence:
            code_lines.append(lines[i])
            i += 1
        if i < n:
            i += 1  # skip the closing fence line

        # ── Step 7: write the reconstructed file ──────────────────────────────
        dest: Path = dest_dir / rel_path

        # WHY: second path-traversal guard after joining — the resolved dest must
        #      still sit inside dest_dir even after symlink resolution.
        if not dest.resolve().is_relative_to(dest_dir):
            logger.warning("Skipping unsafe path (traversal detected): %s", rel_path)
            continue

        code_content: str = "\n".join(code_lines)
        if not code_content.endswith("\n"):
            code_content += "\n"

        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(code_content, encoding="utf-8")
        file_count += 1
        logger.info("Restored: %s", dest.relative_to(dest_dir))

    logger.info("Recreation complete — %d file(s) written to '%s'.", file_count, dest_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Build mode (default): compile a source tree into a Markdown monolith.\n"
            "Recreate mode (-r): restore files from a previously generated monolith."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # ── Build mode ────────────────────────────────────────────────────────────
    parser.add_argument(
        "-t", "--target", type=Path, default=DEFAULT_TARGET,
        help="Source directory to scan (build mode, default: %(default)s)",
    )
    parser.add_argument(
        "-o", "--output", type=Path, default=None,
        help="Output monolith filename (build mode, default: timestamped .md)",
    )

    # ── Recreate mode ─────────────────────────────────────────────────────────
    parser.add_argument(
        "-r", "--recreate", type=Path, default=None, metavar="MONOLITH",
        help="Path to a monolith .md file to restore files from (activates recreate mode)",
    )
    parser.add_argument(
        "-d", "--dest", type=Path, default=Path("recreated"),
        help="Destination directory for restored files (recreate mode, default: ./recreated)",
    )

    args = parser.parse_args()

    if args.recreate is not None:
        recreate_from_monolith(args.recreate, args.dest)
    else:
        output: Path = stamp_output_path(args.output) if args.output is not None else default_output_name()
        compile_monolith(args.target, output)
