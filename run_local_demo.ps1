$env:DEBUG = "False"
Set-Location -LiteralPath $PSScriptRoot
& "$PSScriptRoot\venv\Scripts\python.exe" "$PSScriptRoot\backend\run_demo.py"
