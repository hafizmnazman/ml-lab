# Getting started

The configured project uses **Python 3.12 + `.venv`**. This is Route A in
the course setup handout; Anaconda is optional. Packages are isolated from
the existing global Python installation. PyTorch can be added for Labs 7-8
using `requirements-later-labs.txt`.

## Open the labs on this computer

Double-click **`start-lab.cmd`** in the project folder. It starts JupyterLab
and opens your browser. Open either notebook in `all_experiments/` and choose
**Python (ml-lab)** in the kernel selector. The notebooks already contain
executed outputs. Use **Run > Run All Cells** to repeat a lab, or run one cell
at a time with **Shift+Enter**. Close the terminal or press **Ctrl+C** there
to stop the server.

## Create the environment after cloning

```powershell
git clone https://github.com/hafizmnazman/ml-lab.git
cd ml-lab
powershell -ExecutionPolicy Bypass -File scripts\setup.ps1
.\start-lab.cmd
```

The PowerShell execution-policy flag applies only to that process. The script
creates `.venv`, installs the pinned direct dependencies, and registers the
kernel inside the environment. Add `-UseLock` to install the complete tested
Windows dependency snapshot from `requirements-lock.txt`.

## Run without opening a browser

```powershell
.\.venv\Scripts\python.exe scripts\run_labs.py
.\.venv\Scripts\python.exe scripts\run_labs.py --lab 01
.\.venv\Scripts\python.exe scripts\run_labs.py --lab 02
.\.venv\Scripts\python.exe predict_passenger.py --pclass 2 --sex female --age 30 --fare 20
.\.venv\Scripts\python.exe scripts\verify.py
```

Always use the environment's executable, as shown. Activation is convenient
but unnecessary. If preferred, run `.\.venv\Scripts\Activate.ps1`, then
use `python`. See the [Python venv documentation](https://docs.python.org/3.12/library/venv.html)
and [JupyterLab installation guide](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html).

## Folder arrangement

| Path | Contents |
|---|---|
| `all_datasets/` | Exact supplied course datasets and checksum manifest |
| `all_experiments/` | Lab 01 and Lab 02 worked notebooks |
| `models/` | Locally generated pipelines and committed JSON model cards |
| `results/lab01/`, `results/lab02/` | Measured metrics, tables, charts, and decision memo |
| `course_materials/lab01/`, `course_materials/lab02/` | Original PDFs and starter files, preserved locally |
| `scripts/` | Environment setup, execution, and verification |
| `.github/readme/` | Terminal-style art and screenshots |
| `.venv/`, `.local/` | Local environment and temporary execution files |

The folder on this computer remains `Lab`; the GitHub repository is `ml-lab`.
Avoid moving a configured `.venv`; after moving or renaming the project root,
recreate the environment because virtual environments contain absolute paths.

Original filenames were made readable: `ML-Lab01.pdf` became
`course_materials/lab01/lab01-assignment.pdf`; `ML-Python-Datasets.pdf` became
`environment-and-datasets.pdf`; the Lab 2 assignment and chapter became
`lab02-assignment.pdf` and `chapter04-how-machine-learning-works.pdf`.
The supplied empty Python file and populated duplicate were both preserved;
the working predictor now lives at the project root as required by the course.

## Common fixes

- **Wrong kernel or missing package:** choose Python (ml-lab), then restart
  the kernel. Check the first cell's environment output.
- **Missing model:** execute Lab 02. A fresh clone contains cards and results,
  while binary pipelines are recreated locally.
- **File not found:** start Jupyter with `start-lab.cmd`. The notebooks locate
  datasets from either the root or `all_experiments/`.
- **New lab material:** keep handouts in `course_materials/`, add a worked
  notebook to `all_experiments/`, and write its evidence to `results/labNN/`.
