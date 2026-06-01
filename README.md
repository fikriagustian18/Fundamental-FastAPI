# Fundamental FastAPI - Dependency Injection, Pydantic Models, and Background Tasks

This repository is designed to help you understand the fundamental concepts of FastAPI, specifically its three key pillars: **Dependency Injection**, **Pydantic Models**, and **Background Tasks**. This project features a modular, ready-to-use, and easy-to-understand code structure.

---

## System Requirements
Before starting, make sure your device meets the following minimum specifications:
* **Python**: Version 3.11 or newer.
* **Operating System**: Windows, macOS, or Linux.
* **Package Manager**: `pip` (standard with Python).

---

## Installation & Setup

### 1. Install Project Dependencies
Install all required packages listed in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
This application uses Pydantic Settings to load configurations from a `.env` file. A standard `.env` file is already provided in the root directory with default configurations:
```env
PREFIX_VERSION=/api/v1
VERSION=1.0.0
APP_HOST=localhost
APP_PORT=8000
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
```
*(You can customize the host or port in this file according to your needs).*

---

## How to Run the Application

Since `app/main.py` is already configured with a `__main__` block, you can run it directly using Python:
```bash
python -m app.main
```

Once the server runs successfully, the terminal will display logs similar to the following:
`INFO:     Uvicorn server running on http://localhost:8000 (Press CTRL+C to quit)`

---

## Project Structure

Here is a general overview of the project's directory structure:
```text
fundamental_fastapi/
├── app/                                # Main Application Directory
│   ├── api/                            # API Routes and Dependencies Module
│   │   ├── routes/                     # Endpoint Definitions (Controllers)
│   │   │   └── dependency_injection.py # DI & Login Endpoints
│   │   ├── simple_deps.py              # Simple Dependency Functions (Query Params, Form Data)
│   │   └── authentication_deps.py      # Authentication Dependencies (Verify User, JWT)
│   ├── core/                           # Core Application Configuration
│   │   ├── settings.py                 # Pydantic Settings Configuration (.env)
│   │   └── exceptions.py               # Custom Exception & Global Handler
│   ├── crud/                           # Data Access Layer
│   │   └── users.py                    # User CRUD Operations (Dummy DB)
│   └── main.py                         # FastAPI Application Entry Point
├── .env                                # Local Environment Variables
├── .env.example                        # Environment Variables Template
└── requirements.txt                    # Python Dependencies List
```

---

## API Endpoints

FastAPI automatically provides exceptional interactive documentation. Once the application is running, you can access it in your browser via the following links:
* **Swagger UI (Interactive):** [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc (Clean & Structured):** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Dependency Injection (DI) in FastAPI

### Concept
Dependency Injection in FastAPI is used to:
* **Manage shared logic** (such as authentication, database connections, or configurations).
* **Avoid code duplication** (DRY - Don't Repeat Yourself).
* **Make the code more modular & easy to test (testable)**.

FastAPI uses the `Depends()` function to automatically inject dependencies.

### Implementation Example
In this project, we define a simple dependency in [simple_deps.py](app/api/simple_deps.py):

```python
async def common_params(query: str = None, limit: int = 10):
    return { "query": query, "limit": limit }
```

This dependency is then injected into the route inside [dependency_injection.py](app/api/routes/dependency_injection.py):

```python
@router.get("/items/")
async def read_items(commons: dict = Depends(common_params)):
    return commons
```

**Explanation:**
* `common_params` is the **dependency**.
* `Depends(common_params)` will be automatically invoked by FastAPI when the endpoint is accessed, and its return value will be passed into the `commons` parameter.

### Example 2: Form Data Dependency
Dependencies can also be used to extract form data:

```python
async def form_data_params(username: str = None, password: str = None):
    return { "username": username, "password": password }
```

Used in the `/login` endpoint to extract login data from the request body.
