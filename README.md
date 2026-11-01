# AWS Cloud Task API

A containerized REST API built with **Python, FastAPI, PostgreSQL, and Docker**, deployed on **AWS EC2**. This project demonstrates backend development, database integration, containerization, automated testing, and cloud deployment.

## Project Overview

AWS Cloud Task API is a task management REST API that allows users to create, retrieve, update, and delete tasks.

The application uses FastAPI for the backend, PostgreSQL for persistent data storage, and Docker Compose to orchestrate the application and database containers.

## Architecture

The application runs on an AWS EC2 instance using Docker Compose to manage the API and database containers.

```text
             Client
                |
                v
       FastAPI Application
          (Port 8000)
                |
                v
           PostgreSQL
          (Port 5432)

          Docker Compose
                |
                v
             AWS EC2
```


## Tech Stack

| Category | Technology |
|---|---|
| Backend | Python 3.12, FastAPI |
| Database | PostgreSQL 16 |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Containerization | Docker, Docker Compose |
| Testing | Pytest, HTTPX |
| CI/CD | GitHub Actions |
| Cloud Infrastructure | AWS EC2 |
| API Documentation | Swagger UI (OpenAPI) |

## Features

- Create new tasks.
- Retrieve all tasks.
- Retrieve a task by ID.
- Update existing tasks.
- Delete tasks.
- Health check endpoint with database connectivity status.
- Persistent PostgreSQL storage using Docker volumes.
- Automated tests using Pytest.
- Automated test execution through GitHub Actions.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Root endpoint |
| GET | `/health` | Application and database health check |
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{id}` | Retrieve a task by ID |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

### Example: Create a Task

**Request**

```http
POST /tasks
Content-Type: application/json
```

```json
{
  "title": "Learn AWS",
  "description": "Build a cloud-native API",
  "completed": false
}
```

**Response**

```json
{
  "id": 1,
  "title": "Learn AWS",
  "description": "Build a cloud-native API",
  "completed": false
}
```

## Getting Started

### Prerequisites

Make sure you have installed:

- Docker Desktop
- Docker Compose
- Git

No local Python installation is required when running the application using Docker.

### 1. Clone the Repository

```bash
git clone https://github.com/alfinabrar/aws-cloud-task-api.git
cd aws-cloud-task-api
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
POSTGRES_PASSWORD=your_secure_password
```

### 3. Run with Docker Compose

```bash
docker compose up -d --build
```

This starts two containers:

- `task-api`: FastAPI application.
- `task-postgres`: PostgreSQL database.

### 4. Access the API

Open the following URLs:

- API: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/health`

### 5. Stop the Containers

```bash
docker compose down
```

To remove the database volume as well:

```bash
docker compose down -v
```

**Warning:** Removing the volume deletes the persisted PostgreSQL data.

## Running Tests

Run the automated test suite inside the API container:

```bash
docker compose exec api python -m pytest -v
```

The project includes tests for:

- Root endpoint.
- Health check.
- Task creation.
- Task retrieval.
- Non-existent task handling.

GitHub Actions automatically runs the test suite when changes are pushed to the `main` branch or when a pull request targets `main`.

## AWS EC2 Deployment

The application has been deployed to an AWS EC2 instance using Amazon Linux 2023.

Deployment setup:

1. Provisioned an EC2 instance.
2. Installed Docker and Docker Compose.
3. Cloned the GitHub repository.
4. Configured environment variables on the EC2 instance.
5. Built and started the application using Docker Compose.
6. Verified the API and PostgreSQL connectivity.
7. Tested task creation and retrieval on the deployed application.

The API is bound to the EC2 localhost interface and can be accessed remotely through an SSH tunnel.

## Project Structure

```text
aws-cloud-task-api/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
├── tests/
│   └── test_main.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## What I Learned

Through this project, I gained hands-on experience with:

- Building REST APIs using FastAPI.
- Integrating PostgreSQL with SQLAlchemy.
- Containerizing applications using Docker.
- Managing multi-container applications with Docker Compose.
- Writing automated API tests using Pytest.
- Implementing CI workflows using GitHub Actions.
- Deploying containerized applications on AWS EC2.
- Managing application configuration and environment variables.

## Author

**Alfin Abrar Putra**

GitHub: [@alfinabrar](https://github.com/alfinabrar)

---

*This project was built as a hands-on learning project to explore backend development and cloud infrastructure.*
