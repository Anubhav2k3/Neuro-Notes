#!/bin/bash

# Neuro Notes Deployment Script
# Usage: ./deploy.sh [development|production]

set -e

MODE=${1:-development}

echo "🚀 Deploying Neuro Notes in $MODE mode..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if docker-compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "📋 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env file with your configuration before continuing."
    echo "Press Enter when ready..."
    read
fi

if [ "$MODE" = "production" ]; then
    echo "🏭 Starting production deployment..."
    
    # Build and start services
    docker-compose -f docker-compose.yml up --build -d
    
    # Wait for database to be ready
    echo "⏳ Waiting for database to be ready..."
    sleep 10
    
    # Run migrations
    echo "🔄 Running database migrations..."
    docker-compose exec web python manage.py migrate
    
    # Collect static files
    echo "📦 Collecting static files..."
    docker-compose exec web python manage.py collectstatic --noinput
    
    echo "✅ Production deployment complete!"
    echo "🌐 Application is running at http://localhost"
    
else
    echo "🛠️  Starting development deployment..."
    
    # Build and start services
    docker-compose up --build
    
fi

echo "📊 To view logs: docker-compose logs -f"
echo "🛑 To stop: docker-compose down"
echo "🔄 To restart: docker-compose restart"