#!/bin/bash

# Simple script to run Neuro Notes locally
# Usage: ./run_local.sh

echo "🚀 Starting Neuro Notes locally..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install django google-genai

# Run migrations
echo "🗄️ Setting up database..."
python manage.py migrate

# Start server
echo "🌐 Starting server at http://localhost:8000"
echo "Press Ctrl+C to stop"
python manage.py runserver