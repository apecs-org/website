FROM node:20 AS static
LABEL maintainer="Axel Schlindwein <axel.schlindwein@uit.no>"

WORKDIR /usr/src/apecs
COPY package*.json ./
RUN npm ci --include=dev

COPY . .
RUN npm run build
RUN rm -rf apecs/*/static package*.json node_modules

FROM python:3.11-slim
LABEL maintainer="Axel SChlindwein <axel.schlindwein@uit.no>"

SHELL ["/bin/sh", "-eux", "-c"]

WORKDIR /apecs

ENV DJANGO_SETTINGS_MODULE=apecs.settings.prod
ENV DEBIAN_FRONTEND=noninteractive
USER root

RUN apt-get update
RUN apt-get install -y gcc python3-dev libjpeg-dev zlib1g-dev
#RUN apt-get install -y gunicorn3

# Create user
RUN useradd --create-home apecs
USER apecs
WORKDIR /home/apecs

# Setup poetry
RUN pip install poetry

ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=1
ENV POETRY_VIRTUALENVS_CREATE=1
ENV POETRY_CACHE_DIR=/tmp/poetry_cache

# Copy pyproject.toml file
COPY pyproject.toml ./
COPY poetry.lock ./

# Install requirements
RUN python -m poetry install


COPY --from=static --chown=apecs /usr/src/apecs ./

RUN APECS_ALLOWED_HOSTS="" python -m poetry run python manage.py collectstatic --no-input && rm -rf apecs/*/static

RUN chmod +x ./docker-entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["./docker-entrypoint.sh"]