"""Execute the worked notebooks with their own project-local Python kernel."""
import argparse
import asyncio
import json
import os
from pathlib import Path
import sys
import time

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = {
    "01": "lab01_features_worked.ipynb",
    "02": "lab02_supervised_workflow_worked.ipynb",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lab", choices=NOTEBOOKS, help="omit to run both labs")
    args = parser.parse_args()
    if sys.prefix == sys.base_prefix:
        parser.error("Run this with .venv/Scripts/python.exe (Windows) or .venv/bin/python.")
    # Keep connection files and the kernel spec inside this project.
    local = ROOT / ".local"
    kernel_dir = local / "jupyter" / "kernels" / "ml-lab"
    kernel_dir.mkdir(parents=True, exist_ok=True)
    (kernel_dir / "kernel.json").write_text(json.dumps({
        "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
        "display_name": "Python (ml-lab)", "language": "python",
    }), encoding="utf-8")
    os.environ["JUPYTER_PATH"] = str(local / "jupyter")
    os.environ["JUPYTER_RUNTIME_DIR"] = str(local / "jupyter_runtime")
    os.environ["MPLCONFIGDIR"] = str(local / "matplotlib")
    selected = [args.lab] if args.lab else list(NOTEBOOKS)
    for lab in selected:
        path = ROOT / "all_experiments" / NOTEBOOKS[lab]
        notebook = nbformat.read(path, as_version=4)
        start = time.monotonic()
        print(f"Running Lab {lab}: {path.name}", flush=True)
        client = NotebookClient(notebook, timeout=900, kernel_name="ml-lab",
                                resources={"metadata": {"path": str(path.parent)}})
        try:
            client.execute()
        except Exception:
            # Keep an inspectable failure copy; don't replace the last successful notebook.
            nbformat.write(notebook, local / f"failed_lab{lab}.ipynb")
            raise
        nbformat.write(notebook, path)
        errors = [output for cell in notebook.cells for output in cell.get("outputs", [])
                  if output.get("output_type") == "error"]
        if errors:
            raise RuntimeError(f"Lab {lab} has notebook errors")
        print(f"Lab {lab}: complete, no cell errors ({time.monotonic() - start:.1f}s)", flush=True)


if __name__ == "__main__":
    main()
