# Python Basic Project Boilerplate

A minimal Python project structure for general-purpose applications.

## Structure

```
project_name/
├── src/
│   └── __init__.py
├── tests/
│   └── __init__.py
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── README.md
└── .env.example
```

## Usage

1. Copy this structure to your new project
2. Replace `project_name` with your actual project name
3. Install dependencies: `pip install -r requirements.txt`
4. Install dev dependencies: `pip install -r requirements-dev.txt`
5. Run tests: `pytest tests/`

## Features

- Clean project structure
- Separated dev and production dependencies
- Pre-configured for testing with pytest
- Environment variable support
- Git-ready with .gitignore
