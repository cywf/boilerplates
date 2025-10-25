# FastAPI Application Boilerplate

Modern, fast, and production-ready FastAPI application structure.

## Structure

```
fastapi_app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── models/
│   ├── schemas/
│   └── db/
├── tests/
├── requirements.txt
├── .env.example
└── README.md
```

## Features

- Async/await support
- API versioning
- Automatic OpenAPI documentation
- Pydantic data validation
- Dependency injection
- CORS middleware
- Authentication ready
- Database integration
- Testing with pytest-asyncio

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and configure
3. Run development server: `uvicorn app.main:app --reload`
4. Access API docs: http://localhost:8000/docs
5. Run tests: `pytest`

## Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /docs` - Swagger UI documentation
- `GET /redoc` - ReDoc documentation
