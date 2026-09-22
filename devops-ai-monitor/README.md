DevOps AI Monitor

A small monitoring and log-analysis service built as a DevOps/SRE portfolio project.

The service receives application logs through a REST API, determines the severity of an event and returns a recommended action.

Features

* REST API with FastAPI
* log severity analysis
* health check endpoint
* Prometheus metrics
* Docker containerization
* PostgreSQL and Redis services
* automated tests
* GitHub Actions CI
* Docker Compose
* Swagger API documentation

Architecture

                 Client
                   │
                   ▼
              ┌──────────┐
              │ FastAPI  │
              └────┬─────┘
                   │
             ┌─────┴─────┐
             ▼           ▼
       ┌──────────┐ ┌──────────┐
       │ Analyzer │ │ Metrics  │
       └──────────┘ └──────────┘
             │
       ┌─────┴─────┐
       ▼           ▼
 PostgreSQL      Redis

Tech Stack

Technology Purpose
Python Application
FastAPI REST API
PostgreSQL Database
Redis Cache / messaging
Docker Containerization
Docker Compose Local infrastructure
Prometheus Metrics
Pytest Testing
GitHub Actions CI

Run locally

Clone the repository:

git clone https://github.com/qwaddeas/devops-ai-monitor.git
cd devops-ai-monitor

Start the infrastructure:

docker compose up --build

The API will be available at:

http://localhost:8000

Swagger documentation:

http://localhost:8000/docs

Health check:

http://localhost:8000/health

Prometheus metrics:

http://localhost:8000/metrics

API example

Send a log event:

curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "service": "payment-service",
    "message": "Database connection refused"
  }'

Response:

{
  "service": "payment-service",
  "message": "Database connection refused",
  "analysis": {
    "level": "critical",
    "confidence": 0.95,
    "recommendation": "Check service availability and infrastructure immediately."
  }
}

Health Check

curl http://localhost:8000/health

Response:

{
  "status": "ok",
  "service": "devops-ai-monitor"
}

Testing

Run tests locally:

pytest -v

Tests are also executed automatically by GitHub Actions on every push and pull request.

CI Pipeline

Git Push
   │
   ▼
GitHub Actions
   │
   ├── Install dependencies
   │
   ├── Run tests
   │
   └── Build Docker image

DevOps Concepts Demonstrated

This project demonstrates practical knowledge of:

* containerization
* CI automation
* service health checks
* application metrics
* infrastructure dependencies
* automated testing
* environment configuration
* reproducible local development
* REST API development

Future Improvements

Possible next steps:

* Kubernetes deployment
* Helm chart
* Grafana dashboard
* Prometheus alerting
* Telegram notifications
* centralized logging
* Docker image publishing
* deployment to a cloud VM

Author

Developer / DevOps Engineer

Portfolio project demonstrating backend and DevOps engineering practices.