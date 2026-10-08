"""Check execution evidence, data integrity, split isolation, and saved-model CLI."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import nbformat
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    manifest = json.loads((ROOT / "all_datasets/manifest.json").read_text(encoding="utf-8"))
    for item in manifest["files"]:
        path = ROOT / "all_datasets" / item["file"]
        require(path.is_file(), f"Dataset missing: {path.name}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"],
                f"Source dataset changed: {path.name}")
    print(f"[ok] {len(manifest['files'])} dataset checksums")
    for path in sorted((ROOT / "all_experiments").glob("*.ipynb")):
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
        code_cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
        require(all(cell.execution_count is not None for cell in code_cells), f"Unexecuted cells: {path.name}")
        require(not any(o.output_type == "error" for cell in code_cells for o in cell.outputs),
                f"Notebook cell error: {path.name}")
        print(f"[ok] {path.name}: {len(code_cells)} executed code cells, zero errors")
    dev = set(pd.read_csv(ROOT / "results/lab02/titanic_development_rows.csv")["row_index"])
    test = set(pd.read_csv(ROOT / "results/lab02/titanic_test_rows.csv")["row_index"])
    rows = len(pd.read_csv(ROOT / "all_datasets/titanic_dataset.csv"))
    require(dev.isdisjoint(test), "Development and final test overlap")
    require(dev | test == set(range(rows)), "Titanic split does not cover the source rows")
    print(f"[ok] Titanic: {len(dev)} development / {len(test)} final test rows, disjoint and complete")
    report = json.loads((ROOT / "results/lab02/summary.json").read_text(encoding="utf-8"))
    card = json.loads((ROOT / "models/titanic_survival_card.json").read_text(encoding="utf-8"))
    require(card["final_test_roc_auc"] == round(report["titanic_final"]["test_roc_auc"], 4),
            "Model card and run summary disagree")
    require(report["saved_model_reload_matches"], "Saved-model reload check failed")
    high, low = report["cancer_thresholds"]
    require(low["fn"] <= high["fn"] and low["fp"] >= high["fp"], "Threshold counts are inconsistent")
    print("[ok] Model card, reload evidence, and threshold confusion counts")
    predictor = ROOT / "predict_passenger.py"
    command = [sys.executable, str(predictor), "--pclass", "2", "--sex", "female", "--age", "30", "--fare", "20"]
    # Test file resolution from an unrelated working directory.
    with tempfile.TemporaryDirectory(dir=ROOT / ".local") as cwd:
        run = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
        require(run.returncode == 0, f"Prediction CLI failed: {run.stderr}")
        require("survival probability:" in run.stdout, "Prediction CLI output missing")
        invalid = subprocess.run(command + ["--sibsp", "-1"], cwd=cwd, capture_output=True, text=True)
        require(invalid.returncode != 0 and "nonnegative" in invalid.stderr, "Negative counts must be rejected")
    print("[ok] Prediction CLI from another directory; invalid passenger input rejected")
    print("All verification checks passed.")


if __name__ == "__main__":
    main()
