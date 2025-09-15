@echo off
REM === Configuración de rutas ===
set "PROJECT_DIR=D:\Documentos\02-MLR\01-SRC\MyPortfolio\etl-myportfolio"
set "VENV_DIR=%PROJECT_DIR%\.venv"
set "LOG_DIR=%PROJECT_DIR%\logs"

if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"
set "DATESTAMP=%DATE:~-4%%DATE:~3,2%%DATE:~0,2%"

cd /d "%PROJECT_DIR%"
call "%VENV_DIR%\Scripts\activate.bat"
python -m app.wrapper >> "%LOG_DIR%\etl_%DATESTAMP%.log" 2>&1
