@echo off
setlocal enabledelayedexpansion

:: Set default values
set PORT=1984
set DEBUG=false
set isNextPORT=false

:: For each argument (%%A) in all args (%*)
for %%A in (%*) do (
    if !isNextPORT!==true (
        set PORT=%%A
        set isNextPORT=false
    ) else (
        :: logical operators don't exist in batch :(
        if "%%A"=="--debug" set DEBUG=true
        if "%%A"=="-d" set DEBUG=true
        if "%%A"=="--port" set isNextPORT=true
        if "%%A"=="-p" set isNextPORT=true        
    )
)

:: Show debug info
if !DEBUG!==true (
    echo Debug mode: %DEBUG%
    echo custom Port: %PORT%
)

:: Run server.py and app.py 
start "Server" cmd /k python server.py
start "Main App" cmd /k python app.py

:: Open browser
start http://localhost:5000