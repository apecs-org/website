### Stack and external services

#### Analytics

Posthog

#### Error monitoring

Sentry

#### Database

PostgreSQL

#### static files

dev:
tailwindcss

prod:
Whitenoise

#### Media storage

S3 compatible block storage at Hetzner

#### Asynchronous tasks

Redis + Celery

# Setup for development and testing

## Overview

APECS is a Django-based web application with modern frontend tooling, asynchronous task processing, and cloud
integrations. It requires multiple background services to run, e.g. PostgreSQL and Redis.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.13**
- **Poetry** for Python environment management
- **Node.js 16+** and **npm** for JavaScript dependencies
- **Docker**  to run background services, e.g. PostgreSQL and Redis

## Initial Setup

### 1. Clone the Repository

```bash
git clone <repository-url> cd apecs
```

### 2. Python Environment Setup

Install Poetry if not already available:

```bash
pip install poetry
```

Install Python dependencies:

```bash
poetry install
```

### 3. Node.js Dependencies

Install JavaScript dependencies:

```bash
npm install
```

### 6. Django Setup

Run database migrations:

```bash
poetry run dotenv run python manage.py migrate
``` 

Create a superuser:

```bash
poetry run dotenv run python manage.py createsuperuser
``` 

Load fixtures (if available):

```bash
poetry run dotenv run python manage.py loaddata fixture.json
``` 

## Running the Development Environment

You need to run multiple processes concurrently. It's recommended to use separate terminal windows/tabs for each:

### Terminal 1: Django Development Server

```bash
poetry run dotenv run python manage.py runserver
``` 

The application will be available at: `http://localhost:8000`

### Terminal 2: Tailwind CSS Watch Mode

Use ```npm run watch:css``` to make tailwindcss watch for changes:

```bash
npx tailwindcss -i ./apecs/static/src/style.css -o ./apecs/static/dist/style.css --minify --watch
```

### Terminal 3: Webpack Dev Server (Optional)

With ```npm run dev``` you can serve frontend assets with webpack:

```bash
npx webpack serve --mode development
```

## Using Docker Compose (Alternative)

Start services for Redis, Celery and PostgreSQL in the background:

```bash
docker-compose up -d
```

## Common Development Commands

### Django Management

```bash
#Create new migrations
poetry run dotenv run python manage.py makemigrations

#Apply migrations
poetry run dotenv run python manage.py migrate

#Create superuser
poetry run dotenv run python manage.py createsuperuser

#Django shell
poetry run dotenv run python manage.py shell

#Run tests
poetry run dotenv run python manage.py test

#Create a new Django app
poetry run dotenv run python manage.py startapp app_name
```

### Celery Management

```bash
#Purge all tasks
celery -A apecs purge

#Inspect active tasks
celery -A apecs inspect active

#Monitor tasks in real-time
celery -A apecs events
``` 

## Integrations and External Services

### Analytics

- **PostHog**: User analytics and feature flags

### Error Monitoring

- **Sentry**: Error tracking and performance monitoring

### Media Storage

- **Hetzner Object Storage**: S3-compatible object storage for media files

### Static Files

- **Development**: Tailwind CSS with watch mode
- **Production**: Whitenoise for serving static files

### Asynchronous Tasks

- **Redis + Celery**: Background task processing and scheduling

## Production Deployment

Build Docker image:

```bash
docker build . -t apecs --no-cache
``` 

Run production container:

```bash 
docker run -p 8000:8000 --env-file .env apecs
```

## License

See LICENSE.md file for details.
