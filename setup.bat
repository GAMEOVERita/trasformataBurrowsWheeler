:venvWscripts
    python -m venv venv
    .\venv\Scripts\python.exe -m pip install --upgrade pip
    .\venv\Scripts\python.exe -m pip install -r requirements.txt
EXIT /B 0
:venvWOscripts
    python -m venv venv
    .\venv\bin\python.exe -m pip install --upgrade pip
    .\venv\bin\python.exe -m pip install -r requirements.txt
EXIT /B 0

@echo off

::if venv directory exist do nothing, else install the required packages
IF EXIST .\venv (
    ECHO dependencies already installed
    ) ELSE (
        IF EXIST .\venv\Scripts (CALL :venvWscripts) ELSE (CALL :venvWOscripts)
    )