@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Create the environment first: powershell -ExecutionPolicy Bypass -File scripts\setup.ps1
  pause
  exit /b 1
)
set "JUPYTER_RUNTIME_DIR=%~dp0.local\jupyter_runtime"
set "JUPYTER_CONFIG_DIR=%~dp0.local\jupyter_config"
set "MPLCONFIGDIR=%~dp0.local\matplotlib"
".venv\Scripts\python.exe" -m jupyterlab --ServerApp.root_dir="%~dp0." --LabApp.default_url=/lab/tree/all_experiments
