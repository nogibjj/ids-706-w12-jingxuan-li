[![Build and Push Docker Image](https://github.com/nogibjj/ids-706-w12-jingxuan-li/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/ids-706-w12-jingxuan-li/actions/workflows/cicd.yml)
# Simple Python Application with Docker

This is a simple Python application that demonstrates how to containerize an application using Docker and build and push the Docker image in a CI/CD pipeline.

## Table of Contents

- [Application Setup](#application-setup)
- [Dockerfile](#dockerfile)
- [Makefile Commands](#makefile-commands)
- [Running the Application](#running-the-application)
- [CI/CD Pipeline](#cicd-pipeline)

## Application Setup

A Flask application defined in `app.py`:


## Dockerfile

A Dockerfile is already set up to containerize the application:

## Makefile Commands

The `Makefile` provides several commands to manage the Docker image and container:


- **build**: Builds the Docker image.
- **run**: Runs the Docker container.
- **clean**: Removes the Docker image.
- **image_show**: Lists Docker images.
- **container_show**: Lists running Docker containers.
- **push**: Tags and pushes the Docker image to Docker Hub.
- **login**: Logs into Docker Hub.

## Running the Application

To run the application using `make`, follow these steps:

1. **Build the Docker image**:

   ```bash
   make build
   ```

2. **Run the Docker container**:

   ```bash
   make run
   ```

   The application will be accessible at `http://localhost:5001`.
The application is a simple Flask app that provides a temperature converter feature. Users can input a temperature in Celsius, and the application will convert it to Fahrenheit and display the result.

- **Input Celsius Temperature**: Users enter the Celsius temperature in a web form.

- **Convert to Fahrenheit**: The application receives the Celsius input, performs the calculation, and converts it to Fahrenheit.


- **Display Result**: The converted Fahrenheit temperature is displayed on the webpage.

  ![image](https://github.com/user-attachments/assets/18c89fcf-ae7f-42c4-8c9b-7522adfc2013)


3. **Show Docker images**:

   ```bash
   make image_show
   ```

4. **Show running Docker containers**:

   ```bash
   make container_show
   ```

5. **Clean up Docker images**:

   ```bash
   make clean
   ```

## CI/CD Pipeline

The CI/CD pipeline is configured to build and push the Docker image automatically when changes are pushed to the `main` branch

