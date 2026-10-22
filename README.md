# Week 1 — Backend Engineering Fundamentals

## Project Overview

This repository documents my Week 1 Backend Engineering training activities. The objective is to learn Git and GitHub workflows, develop REST APIs using FastAPI, connect backend applications to PostgreSQL, implement secure JWT authentication, organize code using a layered architecture, and test API endpoints.

The project is a **JWT-Authenticated Task Management REST API** built with Python, FastAPI, PostgreSQL, SQLAlchemy, Pydantic, and Pytest.

### Project Objectives

- Understand Git and GitHub workflows.
- Develop RESTful APIs using FastAPI.
- Implement CRUD operations using PostgreSQL.
- Apply a layered backend architecture.
- Implement user registration and JWT authentication.
- Restrict task access according to user ownership.
- Write and execute endpoint tests using Pytest.
- Test APIs using Postman and Swagger UI.

---

## Day 1 — Monday: Git Setup and Backend Server

### Objectives

- Configure Git and SSH authentication.
- Clone and manage the training repository.
- Create and manage feature branches.
- Practise commits, pushes, and Pull Requests.
- Run a local FastAPI server.

### Activities

- Configured Git and GitHub SSH authentication.
- Set up the local Python development environment.
- Practised Git commands, commits, branches, and pushing changes.
- Created feature branches to organize development work.
- Started a local FastAPI application.

### Learning Outcomes

- Understood basic Git workflows.
- Learned repository management and version control.
- Practised running a backend application locally.

---

## Day 2 — Tuesday: Branch/PR Workflow and REST API

### Objectives

- Understand branch and Pull Request workflows.
- Practise code review and merging.
- Develop REST API endpoints using FastAPI.
- Return JSON responses.
- Test API requests and responses.

### Activities

- Worked with Git branches and GitHub workflows.
- Practised committing and pushing code changes.
- Created FastAPI endpoints.
- Returned JSON responses from API requests.
- Tested endpoints using Postman and Swagger UI.

### Learning Outcomes

- Understood REST API fundamentals.
- Learned how HTTP requests and JSON responses work.
- Practised collaborative Git workflows.

---

## Day 3 — Wednesday: REST API Design and PostgreSQL CRUD

### Objectives

- Learn REST API design principles.
- Understand HTTP methods and status codes.
- Implement CRUD operations using FastAPI.
- Connect the application to PostgreSQL.
- Organize code using a layered architecture.
- Validate request data and handle API errors.

### REST API Design Principles

- Use resource-based URLs such as `/tasks/` and `/tasks/{task_id}`.
- Use HTTP methods according to their purpose.
- Return appropriate HTTP status codes.
- Validate incoming request data.
- Return meaningful error responses.
- Separate routing, business logic, database access, and validation.

### HTTP Methods

| Method | Purpose                     |
| ------ | --------------------------- |
| GET    | Retrieve resources          |
| POST   | Create a resource           |
| PUT    | Update an existing resource |
| DELETE | Delete a resource           |

### PostgreSQL Database

Created and connected a PostgreSQL database named `fastapi_tasks`.

The initial task table contained the following columns:

```sql
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT FALSE
);

SELECT * FROM tasks ORDER BY id ASC;
```

The database schema was subsequently extended to support task ownership, status, priority, descriptions, deadlines, and timestamps.

### CRUD API Endpoints

| Method | Endpoint           | Description                       | Expected Status |
| ------ | ------------------ | --------------------------------- | --------------- |
| POST   | `/tasks/`          | Create a task                     | 201 Created     |
| GET    | `/tasks/`          | Retrieve the current user's tasks | 200 OK          |
| GET    | `/tasks/{task_id}` | Retrieve a task by ID             | 200 OK          |
| PUT    | `/tasks/{task_id}` | Update a task                     | 200 OK          |
| DELETE | `/tasks/{task_id}` | Delete a task                     | 200 OK          |

Additional responses include:

- `401 Unauthorized` — Missing or invalid authentication.
- `404 Not Found` — Task not found or not accessible to the current user.
- `409 Conflict` — Duplicate username or email.
- `422 Unprocessable Entity` — Invalid request data.

The DELETE endpoint returns a JSON success message with `200 OK`.

### Layered Architecture

- **Main application:** Initializes FastAPI and registers routers.
- **Database layer:** Configures the PostgreSQL connection and database sessions.
- **Models:** Define database table structures.
- **Schemas:** Validate incoming requests and format responses.
- **Repositories:** Handle database operations.
- **Services:** Implement business logic.
- **Routers:** Define API endpoints and HTTP methods.

### Learning Outcomes

- Implemented task CRUD operations.
- Connected FastAPI to PostgreSQL.
- Used SQLAlchemy for database access.
- Applied Pydantic validation.
- Organized the application into separate layers.
- Tested CRUD operations using Postman and Swagger UI.

---

## Day 4 — Thursday: JWT Authentication and Endpoint Testing

### Objectives

- Understand authentication using JSON Web Tokens (JWT).
- Implement user registration and login.
- Secure API endpoints.
- Restrict task access based on user ownership.
- Add task status, priority, deadline, and timestamps.
- Write and run automated endpoint tests using Pytest.

### User Authentication

Implemented user registration and login endpoints.

| Method | Endpoint         | Description                               |
| ------ | ---------------- | ----------------------------------------- |
| POST   | `/auth/register` | Register a new user                       |
| POST   | `/auth/login`    | Authenticate a user and issue a JWT       |
| GET    | `/auth/me`       | Retrieve the authenticated user's details |

Passwords are hashed before storage. Login returns an access token that is used to authenticate protected requests.

### JWT Authentication Workflow

1. A user registers with a username, email, and password.
2. The application securely hashes the password and stores the user.
3. The user logs in with their credentials.
4. The API returns a JWT access token.
5. The client sends the token in the `Authorization` header.
6. The API validates the token before processing protected requests.
7. The authenticated user's ID is used to restrict access to their tasks.

Example authorization header:

```text
Authorization: Bearer <access_token>
```

The configured access token lifetime is 30 minutes.

### User-Specific Task Management

Implemented user ownership for task operations.

Each task is associated with a user through the `user_id` foreign key.

The task repository filters task retrieval by the authenticated user's ID. This ensures that users can view, update, and delete only their own tasks.

### Task Database Fields

| Column         | Purpose                                    |
| -------------- | ------------------------------------------ |
| `id`           | Unique task identifier                     |
| `title`        | Task title                                 |
| `description`  | Detailed task description                  |
| `completed`    | Completion flag retained for compatibility |
| `status`       | Task status                                |
| `priority`     | Task priority                              |
| `due_date`     | Task deadline                              |
| `user_id`      | Task owner                                 |
| `created_at`   | Creation timestamp                         |
| `updated_at`   | Last update timestamp                      |
| `completed_at` | Completion timestamp                       |

Supported task statuses:

- `PENDING`
- `IN_PROGRESS`
- `COMPLETED`

Supported priorities:

- `LOW`
- `MEDIUM`
- `HIGH`
- `URGENT`

### User Database Fields

| Column            | Purpose                    |
| ----------------- | -------------------------- |
| `id`              | Unique user identifier     |
| `username`        | Unique username            |
| `email`           | Unique email address       |
| `hashed_password` | Secure password hash       |
| `role`            | User role                  |
| `is_active`       | Account activation status  |
| `created_at`      | Account creation timestamp |
| `updated_at`      | Last update timestamp      |

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/b29cc964-b3b9-4281-ad1d-1416153c189b" />

### Endpoint Testing with Pytest

Created `tests/test_api.py` to verify endpoint behavior.

The tests cover:

- Root endpoint response.
- Health endpoint response.
- Authentication requirements for task endpoints.
- Protection of GET, POST, PUT, and DELETE task operations.

### Test Execution

Command:

```powershell
python -m pytest tests/test_api.py -v
```

Verified test results:

```text
7 passed, 0 warning
```
<img width="817" height="291" alt="Screenshot 2026-10-22 164940" src="https://github.com/user-attachments/assets/0f6c44bd-189e-4993-89a5-6ab036e78685" />

All seven tests passed successfully. One deprecation warning was reported by the installed testing dependencies.

### Manual API Verification

Tested authentication and task CRUD operations using Swagger UI and Postman.

Verified:

- User registration and login.
- JWT-protected endpoints.
- Task creation and retrieval.
- Task updates and deletion.
- User-specific task access.
- PostgreSQL task persistence.

<img width="1145" height="598" alt="Screenshot 2026-10-22 164152" src="https://github.com/user-attachments/assets/148d8b8a-3a79-4497-ba1a-18856e54d3e4" />
<img width="1332" height="658" alt="Screenshot 2026-10-22 171356" src="https://github.com/user-attachments/assets/ef3896cd-723e-449a-a58c-483e19557c05" />
<img width="865" height="620" alt="Screenshot 2026-10-22 160559" src="https://github.com/user-attachments/assets/d44e3931-a6f1-4061-b916-a22611fa1cf1" />
<img width="859" height="511" alt="Screenshot 2026-10-22 161025" src="https://github.com/user-attachments/assets/7a17d7c2-ac9d-45d1-be3a-bdcfc84fe375" />


### Learning Outcomes

- Implemented JWT-based authentication.
- Learned password hashing and token validation.
- Protected task endpoints.
- Applied user-specific data access.
- Added automated endpoint tests.
- Practised API testing and error handling.

---
<img width="805" height="341" alt="Screenshot 2026-10-22 162847" src="https://github.com/user-attachments/assets/ab93b737-0e2a-4c19-8d3a-d34080508198" />

## Project Structure

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
│   │   ├── task.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── task_schema.py
│   │   └── user_schema.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── task_repository.py
│   │   └── user_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── task_service.py
│   │   └── auth_service.py
│   ├── security/
│   │   ├── __init__.py
│   │   └── jwt.py
│   └── routers/
│       ├── __init__.py
│       ├── task_router.py
│       └── auth_router.py
├── tests/
│   ├── __init__.py
│   └── test_api.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

The `.env` file contains local configuration and secrets. The `.venv/` directory contains the local Python environment. Both should be excluded from Git using `.gitignore`.

---

## Repository Setup

### Clone the Repository

```bash
git clone git@github.com:mrmanishgit/Week1_BackendTask.git
cd Week1_BackendTask
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment on Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### Run the Application

```powershell
python -m uvicorn src.main:app --reload
```

The application runs locally at:

- API base URL: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health endpoint: http://127.0.0.1:8000/health
- OpenAPI schema: http://127.0.0.1:8000/openapi.json

---

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- PyJWT
- pwdlib with Argon2 password hashing
- Pytest
- HTTPX / FastAPI TestClient
- Git and GitHub
- Postman
- Swagger UI / OpenAPI
- Visual Studio Code

---

## Testing and Verification

The application has been tested using Postman, Swagger UI, and Pytest.

Testing activities include:

- Checking API response status codes.
- Verifying JSON request and response bodies.
- Testing task CRUD operations.
- Verifying user registration and login.
- Checking protected endpoint behavior.
- Testing user-specific task access.
- Validating request data.
- Running automated endpoint tests.

Automated test command:

```powershell
python -m pytest tests/test_api.py -v
```

Latest recorded test result: **7 passed, 1 warning**.

---

## Repository

GitHub: https://github.com/mrmanishgit/Week1_BackendTask

---

## Day 4 Progress Summary

During Day 4, I implemented JWT authentication, user-specific task access, and automated endpoint tests using FastAPI and Pytest. I verified the authentication and task CRUD endpoints using Swagger UI and Postman.

The automated endpoint tests currently pass: 7 passed, 0 warning.

## Current Progress


## Current Progress


## Current Progress

 ✅ Git and GitHub workflows practised.
 ✅ FastAPI REST API developed.
 ✅ PostgreSQL database integration completed.
 ✅ Task CRUD endpoints implemented.
 ✅ JWT authentication implemented.
 ✅ User-specific task access configured.
 ✅ Automated endpoint tests executed successfully.



