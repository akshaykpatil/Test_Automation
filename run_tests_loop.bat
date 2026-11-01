@echo off
setlocal EnableExtensions

cd /d "%~dp0" || exit /b 1

set "HEADLESS=false"

if not exist "test-results" mkdir "test-results"

if exist ".venv\Scripts\python.exe" (
    set "PYTHON=.venv\Scripts\python.exe"
) else (
    set "PYTHON=python"
)

set "RUN_ONCE=0"
if /I "%~1"=="--once" set "RUN_ONCE=1"
set /a RUN_NUMBER=0

:run
set "RUN_ID="
for /f %%I in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss_fff"') do set "RUN_ID=%%I"
if not defined RUN_ID (
    echo ERROR: Could not generate a timestamp for this test run.
    exit /b 1
)
set /a RUN_NUMBER+=1
set "REPORT=test-results\pytest-report-%RUN_ID%-%RUN_NUMBER%.html"
set "LOG=test-results\pytest-log-%RUN_ID%-%RUN_NUMBER%.txt"

echo.
echo [%date% %time%] Starting test run %RUN_NUMBER%
echo Browser mode: headed
echo Report: %REPORT%
echo Log:    %LOG%

"%PYTHON%" -m pytest ".\tests" --html="%REPORT%" --self-contained-html > "%LOG%" 2>&1
set "TEST_EXIT_CODE=%ERRORLEVEL%"

>>"%LOG%" echo.
>>"%LOG%" echo Pytest exit code: %TEST_EXIT_CODE%
echo [%date% %time%] Run %RUN_NUMBER% finished with exit code %TEST_EXIT_CODE%.

if "%RUN_ONCE%"=="1" exit /b %TEST_EXIT_CODE%

echo Waiting 5 seconds before the next run. Close this window to stop.
timeout /t 5 /nobreak >nul
goto run
