param([int]$Port = 8763)
$ErrorActionPreference = 'Stop'
$bundledPython = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
if (Test-Path -LiteralPath $bundledPython) { $pythonExecutable = $bundledPython }
else { $pythonExecutable = (Get-Command python -ErrorAction Stop).Source }
& $pythonExecutable (Join-Path $PSScriptRoot 'runtime\ast_server.py') --port $Port
exit $LASTEXITCODE
