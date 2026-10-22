# Week 1 — Backend Engineering Fundamentals

## Overview

This repository documents my Week 1 Backend Engineering training activities. The objective is to learn Git and GitHub workflows, develop backend applications using FastAPI, understand REST API design principles, connect APIs to a local PostgreSQL database, and test API requests and responses.

## Day 1 — Monday: Git Setup and Backend Server

### Objectives

- Configure Git and SSH authentication.
- Clone the training repository.
- Create and manage feature branches.
- Practise committing and pushing code changes.
- Create a Pull Request (PR).
- Run a local FastAPI server.

### Activities

- Configured Git and GitHub SSH authentication.
- Set up the local development environment.
- Practised Git commands, commits, and pushing changes.
- Created feature branches to organise development work.
- Started a local FastAPI server.

## Day 2 — Tuesday: Branch/PR Workflow and REST API

### Objectives

- Understand the Git branch and Pull Request workflow.
- Practise code review and merging.
- Develop REST API endpoints that return JSON responses.
- Test API requests and responses.

### Activities

- Worked with feature branches and GitHub workflows.
- Practised committing and pushing code changes.
- Created FastAPI endpoints.
- Returned JSON responses from API requests.
- Tested endpoints using Postman and Swagger UI.

## Day 3 — Wednesday: REST API Design and PostgreSQL CRUD

### Objectives

- Learn REST API design principles.
- Understand HTTP methods and status codes.
- Build CRUD endpoints using FastAPI.
- Connect the backend application to a local PostgreSQL database.
- Organise the application using a layered architecture.
- Test API functionality using Postman.

### REST API Design Principles

- Use resource-based URLs, such as `/tasks` and `/tasks/{task_id}`.
- Use HTTP methods according to their purpose.
- Return appropriate HTTP status codes.
- Validate incoming request data.
- Handle errors with meaningful HTTP responses.
- Separate routing, business logic, database access, and data validation.

### HTTP Methods

| Method | Purpose                     |
| ------ | --------------------------- |
| GET    | Retrieve resources          |
| POST   | Create a resource           |
| PUT    | Update an existing resource |
| DELETE | Delete a resource           |

### PostgreSQL Database

Created a PostgreSQL `tasks` table to store task information.

```sql
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT FALSE
);

SELECT * FROM tasks;
```

### CRUD API Endpoints

| Method | Endpoint           | Description             | Expected Status |
| ------ | ------------------ | ----------------------- | --------------- |
| POST   | `/tasks`           | Create a new task       | 201 Created     |
| GET    | `/tasks`           | Retrieve all tasks      | 200 OK          |
| GET    | `/tasks/{task_id}` | Retrieve a task by ID   | 200 OK          |
| PUT    | `/tasks/{task_id}` | Update an existing task | 200 OK          |
| DELETE | `/tasks/{task_id}` | Delete a task           | 204 No Content  |

Additional responses include `404 Not Found` when a requested task does not exist and `422 Unprocessable Entity` when request data fails validation.

### Project Structure

```text
Week1 Task/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── task_schema.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── task_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py
│   └── routers/
│       ├── __init__.py
│       └── task_router.py
├── tests/
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── .venv/
```

**Note:** The `tests/` directory is optional unless you have created it. The `.env` file contains local configuration and should not be committed to GitHub.

### Application Architecture

- **Main application:** Initialises FastAPI and registers routers.
- **Database layer:** Configures the PostgreSQL connection and database sessions.
- **Models:** Define the database table structure.
- **Schemas:** Validate incoming requests and format API responses.
- **Repositories:** Handle database CRUD operations.
- **Services:** Implement business logic and error handling.
- **Routers:** Define API endpoints and HTTP methods.

## Repository Setup

### Clone the Repository

```bash
git clone git@github.com:mrmanishgit/Week1_BackendTask.git
cd Week1_BackendTask
```

### Create and Activate a Virtual Environment

If you have not already created one:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Run the Application

For the current `src/` project structure:

```bash
python -m uvicorn src.main:app --reload
```

The application runs locally at:

- API base URL: http://127.0.0.1:8000
- Interactive API documentation: http://127.0.0.1:8000/docs
- OpenAPI schema: http://127.0.0.1:8000/openapi.json

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- Git
- GitHub
- Swagger UI / OpenAPI
- Postman
- Visual Studio Code

## Testing and Verification

- Tested API endpoints using Postman.
- Verified request and response JSON.
- Tested task creation, retrieval, updating, and deletion.
- Checked request validation and HTTP error responses.
- Verified that task data is saved in PostgreSQL.
- Checked that stored records remain available after restarting the application.

## Learning Outcomes

- Configured Git and SSH authentication.
- Learned repository management, feature branching, commits, and pushes.
- Practised Pull Requests and code review workflows.
- Developed and ran a local FastAPI application.
- Understood REST API design principles and HTTP methods.
- Implemented CRUD endpoints connected to PostgreSQL.
- Applied a layered architecture to backend development.
- Used SQLAlchemy for database interaction and Pydantic for data validation.
- Tested API requests and responses using Postman.
- Practised HTTP status-code handling and error management.

## Repository

GitHub: https://github.com/mrmanishgit/Week1_BackendTask
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/fda82516-5802-47ce-806e-17dd45e4a1e5" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/506251b4-8b63-4a01-96e6-189877301045" />
<img width="454" height="218" alt="image" src="https://github.com/user-attachments/assets/26e9a805-ee8f-4d34-87e4-5ac843177829" />
<img width="850" height="597" alt="image" src="https://github.com/user-attachments/assets/44797927-a1b4-4b71-b5da-492023a9818a" />
<img width="642" height="452" alt="image" src="https://github.com/user-attachments/assets/bd063af3-08e5-41e6-89c4-5fc12338ea8f" />
<img width="670" height="444" alt="image" src="https://github.com/user-attachments/assets/a668541b-7d27-4f01-8783-10d086c2f33f" />

## Day 3 Completion Status

The Day 3 assignment is complete when all five CRUD endpoints have been tested successfully in Postman and the operations have been verified against the local PostgreSQL database.
