#!/usr/bin/env python3
"""
Simple setup script for local development
Usage: python setup_local.py
"""

import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"📋 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}: {e.stderr}")
        return False

def setup_local_environment():
    """Set up the local development environment"""
    print("🚀 Setting up Neuro Notes for local development...\n")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        return False
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Create virtual environment
    if not os.path.exists('venv'):
        if not run_command('python -m venv venv', 'Creating virtual environment'):
            return False
    else:
        print("✅ Virtual environment already exists")
    
    # Determine activation command based on OS
    if os.name == 'nt':  # Windows
        activate_cmd = 'venv\\Scripts\\activate'
        pip_cmd = 'venv\\Scripts\\pip'
        python_cmd = 'venv\\Scripts\\python'
    else:  # Unix/Linux/Mac
        activate_cmd = 'source venv/bin/activate'
        pip_cmd = 'venv/bin/pip'
        python_cmd = 'venv/bin/python'
    
    # Install dependencies
    if not run_command(f'{pip_cmd} install django google-genai', 'Installing dependencies'):
        return False
    
    # Run migrations
    if not run_command(f'{python_cmd} manage.py migrate', 'Setting up database'):
        return False
    
    print("\n🎉 Setup complete!")
    print("\n📝 Next steps:")
    print("1. Activate virtual environment:")
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    
    print("2. Start the server:")
    print("   python manage.py runserver")
    print("3. Open http://localhost:8000")
    print("\n💡 Your API key is already configured in settings.py")
    
    return True

if __name__ == '__main__':
    setup_local_environment()