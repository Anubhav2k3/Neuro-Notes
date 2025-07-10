# Neuro Notes - AI-Powered Note Taking Application

An intelligent note-taking application that combines traditional note management with AI-powered features for enhanced productivity.

## Features

- **Smart Note Management**: Create, edit, and organize your notes with an intuitive interface
- **AI-Powered Enhancement**: 
  - Summarize lengthy notes automatically
  - Improve grammar and readability
  - Translate content to Hindi
  - Analyze content for insights and suggestions
- **Beautiful Dark Theme**: Professional minimal design with smooth animations
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Processing**: Instant AI processing with loading indicators

## Technology Stack

- **Backend**: Django 5.2.4
- **AI Integration**: Google Gemini API
- **Database**: SQLite (easily configurable for PostgreSQL)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with modern design principles

## Installation

### Quick Start with Docker (Recommended)

1. Clone the repository:
```bash
git clone <your-repo-url>
cd neuro-notes
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API key and configuration
```

3. Build and run with Docker Compose:
```bash
docker-compose up --build
```

4. Open your browser and navigate to `http://localhost`

### Manual Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd neuro-notes
```

2. Install dependencies:
```bash
pip install django google-genai
```

3. Set up your API key:
   - Get a Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)
   - Update `GEMINI_API_KEY` in `neuro_notes/settings.py`

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Open your browser and navigate to `http://localhost:8000`

## Usage

1. **Create Notes**: Click "New Note" to start writing
2. **AI Features**: While editing, use the toolbar buttons to:
   - Improve grammar and readability
   - Generate summaries
   - Translate to Hindi
   - Analyze content for insights
3. **Manage Notes**: View all notes on the homepage with preview/expand functionality
4. **Edit & Delete**: Use the action buttons on each note card

## Configuration

### Environment Variables
Create a `.env` file based on `.env.example`:

```bash
# Django Settings
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Google Gemini API
GEMINI_API_KEY=your-gemini-api-key-here

# Database (for production)
DATABASE_URL=postgres://user:password@localhost:5432/neuro_notes
```

### Docker Deployment

#### Development
```bash
docker-compose up --build
```

#### Production
```bash
# Build production image
docker build -t neuro-notes .

# Run with production settings
docker run -p 8000:8000 --env-file .env neuro-notes
```

### Manual Deployment
The application is ready for deployment on:
- **Docker**: Use included Dockerfile and docker-compose.yml
- **Heroku**: Push with Heroku CLI
- **Railway**: Connect GitHub repository
- **DigitalOcean App Platform**: Deploy from GitHub
- **AWS ECS/EC2**: Use Docker image
- **Google Cloud Run**: Deploy containerized app

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact: anubhavp2k3@gmail.com