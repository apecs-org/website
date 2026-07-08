# ------------------ STAGE 1: Node / static build ------------------
FROM node:20 AS static
LABEL maintainer="Axel Schlindwein <axel.schlindwein@uit.no>"

WORKDIR /usr/src/apecs

# Copy package files and install dependencies
COPY package*.json ./
RUN npm ci --include=dev

# Copy source and build static assets
COPY . .
RUN npm run build

# Keep only static build artifacts to reduce image size
RUN rm -rf node_modules package*.json

# ------------------ STAGE 2: Python / Django ------------------
FROM python:3.13-slim AS python
LABEL maintainer="Axel Schlindwein <axel.schlindwein@uit.no>"

# System dependencies
RUN apt-get update && apt-get install -y \
        gcc python3-dev libjpeg-dev zlib1g-dev curl \
    && rm -rf /var/lib/apt/lists/*

# Non-root user
RUN useradd --create-home apecsuser
USER apecsuser

WORKDIR /home/apecsuser/apecs

# Install Poetry
ENV POETRY_HOME=/home/apecsuser/.poetry
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN pip install --user poetry
ENV PATH="/home/apecsuser/.local/bin:$PATH"

# ------------------ Copy Node build artifacts first ------------------
COPY --from=static --chown=apecsuser /usr/src/apecs/apecs/static ./apecs/static/

# Copy project metadata and install Python dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project true \
    && poetry install --no-root

# Add virtualenv to PATH
ENV PATH="/home/apecsuser/apecs/.venv/bin:$PATH"

# Copy remaining source code
COPY --chown=apecsuser . .

# Collect static files
RUN APECS_ALLOWED_HOSTS="" poetry run python manage.py collectstatic --no-input

# Make entrypoint executable
RUN chmod +x ./docker-entrypoint.sh

# Expose Django port
EXPOSE 8000

# Default settings
ENV DJANGO_SETTINGS_MODULE=apecs.settings.prod

# Entrypoint
ENTRYPOINT ["./docker-entrypoint.sh"]
