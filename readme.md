# Neuro Notes - AI-Powered Note Taking Application

## Overview

Neuro Notes is a Django-based web application that combines traditional note-taking functionality with AI-powered features. The application allows users to create, edit, and manage notes while leveraging Google's Gemini AI to enhance content through grammar improvement, summarization, translation, and analysis features.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Django 5.2.4 with Python
- **Architecture Pattern**: Model-View-Template (MVT) pattern
- **Database**: SQLite (default Django database for development)
- **AI Integration**: Google Gemini 2.5 Flash model via Google GenAI SDK

### Frontend Architecture
- **Template Engine**: Django Templates
- **Styling**: Custom CSS with CSS Grid and Flexbox
- **JavaScript**: Vanilla JavaScript for interactivity
- **Icons**: Font Awesome 6.0.0
- **Responsive Design**: Mobile-first approach with CSS Grid

### Project Structure
```
neuro_notes/
├── manage.py              # Django management script
├── neuro_notes/           # Main project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI configuration
├── notes/                 # Main application
│   ├── models.py         # Note data model
│   ├── views.py          # View controllers
│   ├── urls.py           # App-specific URLs
│   ├── ai_service.py     # AI integration service
│   └── admin.py          # Django admin configuration
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   └── notes/            # Note-specific templates
└── static/               # Static assets (CSS, JS)
```

## Key Components

### Data Models
- **Note Model**: Core entity with fields for title, content, created_at, and updated_at timestamps
- **Database**: Uses Django ORM with SQLite for data persistence
- **Ordering**: Notes ordered by most recently updated

### AI Service Layer
- **AIService Class**: Centralized service for AI operations
- **Supported Features**:
  - Grammar and readability improvement
  - Content summarization
  - Hindi translation
  - Content analysis (implementation appears incomplete)
- **Error Handling**: Comprehensive error catching with user-friendly messages

### User Interface Components
- **Navigation**: Sticky navbar with branding and quick actions
- **Note Cards**: Grid-based layout with expandable content previews
- **Modals**: Help modal and AI result display
- **Forms**: Create and edit forms with AI-powered toolbar
- **Messages**: Django messages framework for user feedback

### Authentication & Security
- **CSRF Protection**: Enabled for form submissions
- **Trusted Origins**: Configured for Replit domains
- **Debug Mode**: Currently enabled (should be disabled in production)
- **Secret Key**: Using default insecure key (needs production replacement)

## Data Flow

### Note Management Flow
1. User creates/edits note through forms
2. Data validated and saved via Django ORM
3. Success/error messages displayed via Django messages
4. Redirect to appropriate view (list or edit)

### AI Enhancement Flow
1. User selects AI action (grammar, summarize, translate)
2. AJAX request sent to `/ai-action/` endpoint
3. AIService processes content using Gemini API
4. Enhanced content returned and displayed in modal
5. User can accept or reject AI suggestions

### Data Persistence
- SQLite database stores all note data
- Django migrations handle schema changes
- Automatic timestamp tracking for created/updated times

## External Dependencies

### Core Dependencies
- **Django 5.2.4**: Web framework
- **Google GenAI SDK**: AI integration for Gemini API
- **Font Awesome**: Icon library

### Environment Requirements
- **GEMINI_API_KEY**: Required environment variable for AI features
- **Python 3.x**: Backend runtime
- **SQLite**: Database (included with Python)

### Hosting Configuration
- **Replit-specific**: CSRF trusted origins configured for Replit domains
- **ALLOWED_HOSTS**: Configured for local and Replit hosting
- **Static Files**: Served directly (development configuration)

## Deployment Strategy

### Development Setup
- Uses Django's built-in development server
- SQLite database for simplicity
- Debug mode enabled for development
- Static files served by Django

### Production Considerations
- **Security**: Change SECRET_KEY, disable DEBUG mode
- **Database**: Consider PostgreSQL for production
- **Static Files**: Use proper static file serving (WhiteNoise or CDN)
- **Environment Variables**: Secure storage of API keys
- **HTTPS**: Enable for production deployment

### Replit Deployment
- Pre-configured for Replit hosting environment
- CSRF origins set for Replit domains
- Flexible host configuration for Replit's dynamic URLs

## Technical Decisions

### Database Choice
- **SQLite**: Chosen for development simplicity and zero-configuration setup
- **Trade-offs**: Easy to start with but may need migration to PostgreSQL for production scale

### AI Integration
- **Google Gemini**: Selected for advanced language capabilities
- **Service Layer**: Abstracted AI calls into dedicated service for maintainability
- **Error Handling**: Graceful degradation when AI services are unavailable

### Frontend Approach
- **Server-Side Rendering**: Uses Django templates for faster initial loads
- **Progressive Enhancement**: JavaScript adds interactivity without breaking core functionality
- **CSS Grid**: Modern layout approach for responsive design

### State Management
- **Session-based**: Uses Django's built-in session handling
- **No Authentication**: Currently no user authentication system (single-user or public access)
