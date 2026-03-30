@echo off
setlocal
echo Starting UIBuilder AI...

set "ROOT_DIR=%~dp0"
set "UVICORN=%ROOT_DIR%\.venv\Scripts\uvicorn.exe"
set "BACKEND_DIR=%ROOT_DIR%\Backend\app"
set "FRONTEND_DIR=%ROOT_DIR%\frontend"

:: Start Backend in a new CMD window
echo Starting Backend (FastAPI on port 8000)...
start "UIBuilder Backend" cmd /k "cd /d "%BACKEND_DIR%" && "%UVICORN%" api:app --reload --host 127.0.0.1 --port 8000"

timeout /t 2 >nul

:: Start Frontend in a new CMD window
echo Starting Frontend (Vite on port 5173)...
start "UIBuilder Frontend" cmd /k "cd /d "%FRONTEND_DIR%" && npm run dev"

echo.
echo Both servers are starting in separate terminal windows!
echo   Frontend: http://localhost:5173/
echo   Backend:  http://127.0.0.1:8000/
echo.
pause
