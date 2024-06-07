@echo off
call venv\Scripts\activate.bat
cd /d "%~dp0\core"
python main.py
pause