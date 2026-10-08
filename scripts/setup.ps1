param([switch]$UseLock)
$ErrorActionPreference = 'Stop'
$ProjectRoot = Split-Path -Parent $PSScriptRoot
Push-Location -LiteralPath $ProjectRoot
try {
    if (-not (Test-Path -LiteralPath '.venv\Scripts\python.exe')) {
        python -c "import sys; assert sys.version_info[:2] == (3, 12), 'Use Python 3.12 for this project.'"
        if ($LASTEXITCODE -ne 0) { throw 'Python 3.12 is required to create this environment.' }
        python -m venv .venv
        if ($LASTEXITCODE -ne 0) { throw 'Python 3.12 is required to create this environment.' }
    }
    $Requirements = if ($UseLock) { 'requirements-lock.txt' } else { 'requirements.txt' }
    & '.\.venv\Scripts\python.exe' -m pip install -r $Requirements
    if ($LASTEXITCODE -ne 0) { throw 'Package installation failed.' }
    & '.\.venv\Scripts\python.exe' -m ipykernel install --prefix .venv --name ml-lab --display-name 'Python (ml-lab)'
    if ($LASTEXITCODE -ne 0) { throw 'Kernel registration failed.' }
    Write-Host 'Ready. Open notebooks with .\start-lab.cmd or run .\.venv\Scripts\python.exe scripts\run_labs.py'
} finally {
    Pop-Location
}
