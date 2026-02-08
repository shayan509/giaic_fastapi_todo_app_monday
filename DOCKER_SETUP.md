# Docker Setup for Full Stack Application

This guide explains how to build and run the full-stack application using Docker containers.

## Prerequisites

- Docker Engine installed
- Docker Compose installed (if using compose)

## Building and Running Individual Services

### Backend (FastAPI)

To build the backend service:

```bash
cd backend
docker build -t fastapi-backend .
```

To run the backend service:

```bash
docker run -p 8000:8000 fastapi-backend
```

### Frontend (Next.js)

To build the frontend service:

```bash
cd frontend
docker build -t nextjs-frontend .
```

To run the frontend service:

```bash
docker run -p 3000:3000 nextjs-frontend
```

## Running Both Services with Docker Compose

To build and run both services together:

```bash
docker-compose up --build
```

To run in detached mode:

```bash
docker-compose up --build -d
```

To stop the services:

```bash
docker-compose down
```

## Service Configuration

- **Backend**: Runs on port 8000, serves the FastAPI application
- **Frontend**: Runs on port 3000, serves the Next.js application
- **Environment Variables**: The frontend receives `NEXT_PUBLIC_API_URL` to connect to the backend. In Docker Compose, this is set to `http://backend:8000` to use the service name for inter-container communication.

## Files Overview

- **Dockerfile**: Defines how to build the container image for each service
- **.dockerignore**: Specifies files and directories to exclude from the Docker build context
- **docker-compose.yml**: Orchestrates both services together

## Notes

- The backend Dockerfile uses uv for dependency management as per the existing setup
- The frontend Dockerfile implements a multi-stage build for optimal image size
- In production, you may want to adjust the exposed ports and add a reverse proxy