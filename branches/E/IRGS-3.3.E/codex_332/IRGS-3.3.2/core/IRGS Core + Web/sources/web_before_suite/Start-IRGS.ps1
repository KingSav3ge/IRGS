param([int]$Port = 8765)
$ErrorActionPreference = 'Stop'
$irgsPython = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
if (-not (Test-Path -LiteralPath $irgsPython)) { $irgsPython = (Get-Command python -ErrorAction Stop).Source }
Write-Host "Open http://127.0.0.1:$Port in your browser. Press Ctrl+C to stop IRGS."
& $irgsPython (Join-Path $PSScriptRoot 'server.py') --port $Port
