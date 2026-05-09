@echo off
echo ========================================
echo    NWFET Energy Band Diagram Server
echo ========================================
echo.
echo Starting server...
echo.

cd /d "%~dp0"

python manage.py runserver --host 0.0.0.0 --port 8080

pause
