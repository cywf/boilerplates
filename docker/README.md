# Docker Boilerplates

Collection of Dockerfile templates for various technologies.

## Available Templates

### Python
- `python/Dockerfile` - Basic Python application
- `python/Dockerfile.flask` - Flask application
- `python/Dockerfile.fastapi` - FastAPI application

### Node.js
- `nodejs/Dockerfile` - Basic Node.js application
- `nodejs/Dockerfile.express` - Express.js application
- `nodejs/Dockerfile.react` - React application

### Multi-stage
- `multi-stage/Dockerfile.python` - Multi-stage Python build
- `multi-stage/Dockerfile.nodejs` - Multi-stage Node.js build

## Docker Compose

Each template includes a `docker-compose.yml` for easy local development.

## Best Practices

- Use official base images
- Multi-stage builds for smaller images
- Non-root user for security
- Layer caching optimization
- .dockerignore for faster builds
- Health checks included
