@echo off
echo Starting Kolam Generator Backend...
echo.
echo Make sure you have Python installed and pip available.
echo.
cd backend
echo Installing dependencies...
python -m pip install -r requirements.txt
echo.
echo Starting Flask server on http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py
pause
