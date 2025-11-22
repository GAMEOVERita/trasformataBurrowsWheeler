@echo off

:: Opens "server.py"
start "Server" cmd /k python server.py

:: Opens "app.py"
start "Main App" cmd /k python app.py

:: Opens the browser on the page "https://localhost" at the port "5000"
start http://localhost:5000