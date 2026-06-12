@echo off
REM Quick Setup Script for Feedback System

echo ========================================
echo   Feedback System - Setup & Run
echo ========================================
echo.

REM Check if venv exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created!
) else (
    echo Virtual environment already exists.
)

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing requirements...
pip install -r requirements.txt

echo.
echo Running migrations...
python manage.py migrate

echo.
echo Creating superuser (optional - you can skip by pressing Ctrl+C)
python manage.py createsuperuser

echo.
echo ========================================
echo   Starting Django Development Server
echo ========================================
echo.
echo Access the application at: http://127.0.0.1:8000/
echo Access admin panel at: http://127.0.0.1:8000/admin/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver
