# Simple Python Application with Docker

This is a simple Python application that demonstrates how to containerize an application using Docker and build and push the Docker image in a CI/CD pipeline.

## Table of Contents


- [Prerequisites](#prerequisites)
- [Application Description](#application-description)
- [Dockerfile](#dockerfile)
- [Build and Run Docker Container](#build-and-run-docker-container)
- [CI/CD Pipeline](#cicd-pipeline)
- [Push to Docker Hub](#push-to-docker-hub)

## Prerequisites

- Docker installed
- Docker Hub account (or another container management service)

## Application Description

This application is a simple Flask application that provides a temperature converter to convert Celsius to Fahrenheit.

## Dockerfile

Below is the Dockerfile used to containerize the application:

```dockerfile
# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies
RUN pip install flask

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "w12/app.py"]
```

## Build and Run Docker Container

1. **Build the Docker image**:

   ```bash
   docker build -t my-python-app .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 5000:5000 my-python-app
   ```

   Access the application at `http://localhost:5000`.

## CI/CD Pipeline

In your CI/CD pipeline, you can automate the build and push of the Docker image using the following steps:

1. **Build the Docker image**:

   ```bash
   docker build -t my-dockerhub-username/my-python-app:latest .
   ```

2. **Log in to Docker Hub**:

   ```bash
   echo "$DOCKER_HUB_PASSWORD" | docker login -u "$DOCKER_HUB_USERNAME" --password-stdin
   ```

3. **Push the Docker image**:

   ```bash
   docker push my-dockerhub-username/my-python-app:latest
   ```

## Push to Docker Hub

Ensure that you have set up Docker Hub credentials in your CI/CD pipeline to successfully push the image.
