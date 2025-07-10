@echo off
echo 🚀 Starting Neuro Notes locally...

REM Create virtual environment if it doesn't exist
if not exist venv (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies
echo 📥 Installing dependencies...
pip install django google-genai

REM Run migrations
echo 🗄️ Setting up database...
python manage.py migrate

REM Start server
echo 🌐 Starting server at http://localhost:8000
echo Press Ctrl+C to stop
python manage.py runserver

pause