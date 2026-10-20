param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$RuntimeArguments
)
$ErrorActionPreference = 'Stop'
$bundledPython = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
if (Test-Path -LiteralPath $bundledPython) { $pythonExecutable = $bundledPython }
else { $pythonExecutable = (Get-Command python -ErrorAction Stop).Source }
& $pythonExecutable (Join-Path $PSScriptRoot 'runtime\irgs_r9.py') @RuntimeArguments
exit $LASTEXITCODE
