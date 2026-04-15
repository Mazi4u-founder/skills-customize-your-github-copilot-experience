# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a simple REST API using the FastAPI framework that exposes basic CRUD endpoints for an `Item` resource. Students will learn routing, request/response models with Pydantic, and how to run a development server with Uvicorn.

## 📝 Tasks

### 🛠️ Implement a basic REST API

#### Description
Build a FastAPI application that provides endpoints to create, read, update, and delete `Item` objects stored in an in-memory store. Validate input with Pydantic models and return appropriate HTTP status codes.

#### Requirements
Completed program should:

- Use `FastAPI` and `Pydantic` for request/response models
- Implement endpoints: `POST /items`, `GET /items`, `GET /items/{id}`, `PUT /items/{id}`, `DELETE /items/{id}`
- Use an in-memory store (dictionary) to keep items for the session
- Validate inputs and return `404` for missing resources
- Provide a `main` block so the app can be run directly with Python for development
- Be runnable with `uvicorn starter-code:app --reload`

## Starter files

- `starter-code.py` — minimal FastAPI app with example CRUD endpoints
- `requirements.txt` — Python dependencies for the assignment

## How to run

Install dependencies and run the app:

```bash
pip install -r requirements.txt
uvicorn starter-code:app --reload --port 8000
```

Then open `http://127.0.0.1:8000/docs` to explore the interactive API docs.

## Learning outcomes

- Understand how to define routes and models in FastAPI
- Practice JSON request/response handling and HTTP status codes
- Learn to run and test a local API using Uvicorn and Swagger UI
