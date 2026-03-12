# Emotion Detection AI Web Application

## Project Overview

This project is a Flask-based web application that performs emotion
detection on user-input text using a pre-trained transformer model from
Hugging Face.

The system allows users to submit text through a web interface or API
endpoint and returns predicted emotions along with confidence scores.

The application is containerized using Docker and designed for
deployment on Google Cloud Run, with infrastructure managed using
Terraform and CI/CD automation through GitHub Actions.

The goal of this project is to demonstrate the integration of:

-   Natural Language Processing (NLP)
-   Web application development
-   Containerization
-   Cloud deployment
-   Infrastructure as Code (IaC)
-   CI/CD pipelines

------------------------------------------------------------------------

## System Architecture

The system consists of several main components working together.

### Web Application Layer

The application is built using Flask and provides:

-   A web interface where users can input text for emotion detection
-   A REST API endpoint that allows programmatic access to the model
-   A monitoring dashboard displaying application metrics

------------------------------------------------------------------------

### Machine Learning Model

The application uses the Hugging Face transformer model:

**SamLowe/roberta-base-go_emotions**

This model is trained on the GoEmotions dataset and predicts emotional
labels from user text.

------------------------------------------------------------------------

### Containerization

The application is packaged using Docker to ensure consistent
environments between development and deployment.

Two Docker configurations are included:

-   Dockerfile.dev -- development environment
-   Dockerfile.prod -- production deployment

------------------------------------------------------------------------

### Cloud Deployment

The application is deployed on **Google Cloud Run**, which provides:

-   Serverless containers
-   Automatic scaling
-   Managed infrastructure
-   HTTPS endpoints

------------------------------------------------------------------------

### Infrastructure as Code

Infrastructure is managed using **Terraform**, which defines:

-   Cloud Run service configuration
-   Container resources
-   Public access permissions

------------------------------------------------------------------------

### CI/CD Pipeline

A **GitHub Actions workflow** automates:

1.  Building the Docker image
2.  Pushing the image to Google Artifact Registry
3.  Deploying to Cloud Run using Terraform

------------------------------------------------------------------------

## Project Structure

. ├── main.py\
├── requirements.txt\
├── Dockerfile.dev\
├── Dockerfile.prod\
├── README.md

templates/\
├── index.html\
└── monitor.html

static/\
└── style.css

terraform/\
├── main.tf\
├── providers.tf\
├── variables.tf\
└── terraform.tfvars

test/\
├── test_local.py\
├── test_gcr.py\
├── train.py\
└── load.py

------------------------------------------------------------------------

## Application Features

### Emotion Detection

Users submit text and receive:

-   Predicted emotions above a confidence threshold
-   Top emotion probabilities
-   Model configuration details

------------------------------------------------------------------------

### REST API

POST /predict

Example request:

{ "text": "I am really happy today!" }

Example response:

{ "model": "SamLowe/roberta-base-go_emotions", "threshold": 0.5,
"predicted_emotions": \["joy"\] }

------------------------------------------------------------------------

## Monitoring Dashboard

Accessible at:

/monitor

Displays:

-   Total requests
-   Error rate
-   Average latency
-   Last prediction

------------------------------------------------------------------------

## Local Setup

Clone the repository:

git clone `<repository-url>`{=html}

Install dependencies:

pip install -r requirements.txt

Run the application:

python main.py

Open:

http://localhost:8080

------------------------------------------------------------------------

## Docker

Build:

docker build -f Dockerfile.prod -t emotion-ai .

Run:

docker run -p 8080:8080 emotion-ai

------------------------------------------------------------------------

## Testing

Local API:

python test/test_local.py

Cloud Run API:

python test/test_gcr.py

------------------------------------------------------------------------

## Technologies Used

Python\
Flask\
Hugging Face Transformers\
PyTorch\
Docker\
Google Cloud Run\
Terraform\
GitHub Actions