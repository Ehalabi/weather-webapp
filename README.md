# weather-webapp — Project Board

This directory contains a simple **Python Flask web application** that serves weather information.  
It is part of the larger `weather-webapp` project.

## Overview

- Python web application built with Flask
- HTML templates served with Jinja2
- Designed to run locally, in Docker, or deployed via Kubernetes with the [weatherapp Helm chart](https://github.com/Ehalabi/weather-helm)

## Prerequisites

* Python 3.8+ (for local runs)  
* Docker (to build and run container)  
* Kubernetes cluster (if deploying via Helm)  

## Running Locally

Navigate to this directory and run:
```bash
pip install -r ../../requirements.txt
python pages.py
```

The app will be available at: http://localhost:8000

## Building and Running with Docker

From the project root, build the Docker image:
```bash
docker build -t weather-webapp .
```

Run the container:
```bash
docker run -p 8000:8000 weather-webapp
```

Then access the app at: http://localhost:8000

## Deployment

This app is designed to be deployed to Kubernetes using the Helm chart in:
[https://github.com/Ehalabi/weather-helm](https://github.com/Ehalabi/weather-helm)

Refer to that repository for Kubernetes deployment instructions.

---
