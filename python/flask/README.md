# Flask Application Boilerplate

A production-ready Flask application structure with best practices.

## Structure

```
flask_app/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── static/
│   ├── templates/
│   └── utils/
├── tests/
├── config.py
├── requirements.txt
├── .env.example
├── .flaskenv
├── run.py
└── README.md
```

## Features

- Modular application factory pattern
- Blueprint-based routing
- Database integration (SQLAlchemy)
- Environment-based configuration
- Static files and templates
- Testing setup
- CORS support
- Error handling

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and configure
3. Initialize database: `flask db init && flask db migrate && flask db upgrade`
4. Run development server: `flask run`
5. Run tests: `pytest`

## Endpoints

- `GET /` - Home page
- `GET /api/health` - Health check endpoint
