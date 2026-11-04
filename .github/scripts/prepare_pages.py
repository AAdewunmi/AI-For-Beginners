import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


MAX_SITE_BYTES = 900 * 1024 * 1024


def main():
    repo_root = Path(__file__).resolve().parents[2]
    output_dir = Path(sys.argv[1]).resolve()
    if repo_root in output_dir.parents or output_dir == repo_root:
        raise ValueError("The Pages output directory must be outside the repository.")
    output_dir.mkdir(parents=True, exist_ok=False)

    tracked_files = subprocess.run(
        ["git", "-C", str(repo_root), "ls-files", "-z"],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout.split(b"\0")

    total_bytes = 0
    for tracked_file in tracked_files:
        if not tracked_file:
            continue
        relative_path = Path(os.fsdecode(tracked_file))
        if relative_path.parts[0] in {".git", ".github"}:
            continue

        source = repo_root / relative_path
        if not source.is_file():
            continue

        destination = output_dir / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        if relative_path.parts[0] == "translations" and source.suffix == ".ipynb":
            notebook = json.loads(source.read_text(encoding="utf-8"))
            for cell in notebook.get("cells", []):
                if cell.get("cell_type") == "code":
                    cell["outputs"] = []
                    cell["execution_count"] = None
            destination.write_text(
                json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
                encoding="utf-8",
            )
        else:
            shutil.copy2(source, destination)

        total_bytes += destination.stat().st_size
        if total_bytes > MAX_SITE_BYTES:
            raise ValueError(
                f"Prepared Pages site exceeds the 900 MiB safety limit "
                f"({total_bytes / 1024 / 1024:.1f} MiB)."
            )

    print(f"Prepared Pages site: {total_bytes / 1024 / 1024:.1f} MiB")


if __name__ == "__main__":
    main()
