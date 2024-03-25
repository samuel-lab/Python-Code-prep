@echo off

rem Activate the virtual environment
call venv\bin\activate

rem Run the Python script
python3 main.py true

rem Deactivate the virtual environment
deactivate
