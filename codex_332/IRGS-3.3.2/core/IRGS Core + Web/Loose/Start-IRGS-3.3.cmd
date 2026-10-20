@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0Start-IRGS-3.3.ps1" %*
set "irgsExit=%ERRORLEVEL%"
if not "%irgsExit%"=="0" pause
exit /b %irgsExit%
