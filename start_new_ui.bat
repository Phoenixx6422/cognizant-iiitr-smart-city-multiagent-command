@echo off
title Smart City Command Center - New Light UI
cd /d "%~dp0"

REM Make sure the redesigned UI files are in place
if not exist "templates\index.html" (
    echo [ERROR] templates\index.html not found. Copy the new index.html into the templates folder.
    pause
    exit /b 1
)
if not exist "static\css\styles.css" (
    echo [ERROR] static\css\styles.css not found. Copy the new styles.css into static\css.
    pause
    exit /b 1
)
if not exist "static\js\app.js" (
    echo [ERROR] static\js\app.js not found. Copy the new app.js into static\js.
    pause
    exit /b 1
)

REM Use the shared virtual environment if it exists, otherwise fall back to system Python
set "PY=..\.venv\Scripts\python.exe"
if not exist "%PY%" set "PY=python"

echo.
echo  Starting the new Smart City Command Center UI on http://localhost:8002
echo  (the browser opens automatically - press Ctrl+C to stop the server)
echo.

REM start_ui.py launches the server and opens the browser once it is ready
"%PY%" start_ui.py
pause
