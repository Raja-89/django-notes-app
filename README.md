# Django Notes App — Dockerized Deployment

A simple Notes application built with React and Django, deployed locally using Docker Compose. The deployment uses separate containers for Django, MySQL, and Nginx to demonstrate containerization, service networking, persistent storage, and reverse proxy configuration.

> **Acknowledgment:** The application is based on the original [Django Notes App by LondheShubham153](https://github.com/LondheShubham153/django-notes-app). This repository documents my Docker deployment and configuration work.

## Architecture

```text
                 Browser
                    |
                 Port 80
                    |
              +-----------+
              |   Nginx   |
              +-----------+
                    |
             Docker network
                    |
              +-----------+
              |  Django   |
              | Gunicorn  |
              +-----------+
                    |
              Docker network
                    |
              +-----------+
              |   MySQL   |
              +-----------+
                    |
             Persistent volume
```

## Tech Stack

- **Application:** React, Django, Python 3.9
- **Database:** MySQL
- **Containerization:** Docker, Docker Compose
- **Web server / reverse proxy:** Nginx
- **Application server:** Gunicorn

## Prerequisites

- Docker Engine
- Docker Compose v2
- Git

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/LondheShubham153/django-notes-app.git
cd django-notes-app
```

If you have a fork containing your deployment changes, clone your fork instead.

### 2. Configure environment variables

Create or update the `.env` file with the variables expected by the Django project. Configure the database hostname as `db`, the Compose service name.

Do not commit passwords, API keys, or other secrets to Git.

### 3. Start the application

```bash
docker compose up -d --build
```

This builds the application and Nginx images and starts the services in the background.

### 4. Verify the containers

```bash
docker compose ps -a
```

View service logs:

```bash
docker compose logs --tail=50 db django nginx
```

### 5. Access the application

- **Nginx reverse proxy:** http://localhost
- **Django application directly:** http://localhost:8000

The available pages depend on the routes configured in the application.

## Docker Configuration

The Docker Compose deployment includes:

- **Django:** Runs database migrations and serves the application through Gunicorn.
- **MySQL:** Stores application data in a named Docker volume.
- **Nginx:** Acts as a reverse proxy and forwards requests to Django.
- **Bridge network:** Enables communication between containers through Compose service names.
- **Health checks:** Checks MySQL readiness and Django's HTTP response.

## Troubleshooting

### Container name conflict

Inspect existing containers before removing anything:

```bash
docker ps -a
docker inspect mysql
```

### Service connectivity issues

Check service names, network configuration, and logs:

```bash
docker compose config
docker compose logs db django nginx
```

### Rebuild the deployment

```bash
docker compose up -d --build
```

Avoid `docker compose down -v` unless you intentionally want to remove the associated named volumes and their stored data.

## What I Learned

- Containerizing a multi-service web application.
- Orchestrating services with Docker Compose.
- Configuring Nginx as a reverse proxy.
- Connecting application and database containers through Docker networking.
- Persisting MySQL data with named volumes.
- Using health checks, logs, and container inspection to troubleshoot deployment issues.

## Acknowledgment

Original application: [LondheShubham153/django-notes-app](https://github.com/LondheShubham153/django-notes-app)

Tutorial followed: [YouTube deployment tutorial](https://youtu.be/9bSbNNH4Nqw)
# django-notes-app
