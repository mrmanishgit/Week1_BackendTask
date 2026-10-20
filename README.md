# Week 1 — Backend Engineering Fundamentals

Overview

This repository documents my Week 1 Backend Engineering training activities. The objective is to learn Git and GitHub workflows, run a backend server locally, and develop and test REST APIs that return JSON responses.

Day 1 — Monday: Git Setup and Backend Server
 
Objectives

Configure Git and SSH authentication.

Clone the training repository.

Create a feature branch.

Practise committing and pushing code.

Create a Pull Request (PR).

Run a local FastAPI server.

## Day 2 — Tuesday: Branch/PR Workflow and REST API

Objectives

Understand the branch and Pull Request workflow.

Practise code review and merging.

Develop a REST API endpoint that returns JSON.

## Test API requests and responses.

Clone the repository

git clone git@github.com:mrmanishgit/Week1_BackendTask.git
cd Week1_BackendTask

## Install dependencies
python -m pip install -r requirements.txt

## Run the application
python -m uvicorn main:app --reload
The application runs locally at http://127.0.0.1:8000.

Project Structure

Week1 Task/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/                

## Technologies Used

Python ,FastAPI,Git,GitHub,Swagger UI / OpenAPI,Postman,Visual Studio Code

## API endpoints
- GET / - Welcome message
- GET /health - Health check
- GET /docs - Swagger documentation
- GET /tasks/{task_id}-Retrieve a task by ID
- POST /tasks -Create a new task

## Learning Outcomes

Git configuration and SSH authentication.

Repository setup and feature branching.

Committing and pushing code changes.

Understanding Pull Requests and code review workflows.

Running a backend server locally.

Building REST endpoints and returning JSON.

Validating request data and handling errors.

Testing APIs using Swagger UI and Postman.
<img width="1052" height="588" alt="image" src="https://github.com/user-attachments/assets/e22b2043-f45e-4b27-ae9d-37a37d195785" />
