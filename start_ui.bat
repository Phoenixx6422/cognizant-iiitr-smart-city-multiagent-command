@echo off
title smart_city_dashboard UI
cd /d "%~dp0"

REM Use the shared virtual environment if it exists, otherwise fall back to system Python
set "PY=..\.venv\Scripts\python.exe"
if not exist "%PY%" set "PY=python"

REM Open the browser after a short delay so the server has time to start
start "" cmd /c "timeout /t 3 /nobreak >nul & start http://localhost:8002"

"%PY%" server.py
pause
