# Docker Compose Database Templates

Ready-to-use Docker Compose configurations for common databases.

## Available Databases

- **MongoDB** - NoSQL document database
- **PostgreSQL** - Relational database
- **MySQL** - Relational database
- **Redis** - In-memory data store

## Usage

```bash
# Navigate to the database directory
cd database/mongodb  # or postgresql, mysql

# Start the database
docker-compose up -d

# Stop the database
docker-compose down

# View logs
docker-compose logs -f
```

## Features

- Persistent data volumes
- Environment-based configuration
- Health checks
- Resource limits
- Network isolation
- Admin interfaces (where applicable)

## Connection Strings

### MongoDB
```
mongodb://admin:password@localhost:27017/mydb?authSource=admin
```

### PostgreSQL
```
postgresql://postgres:password@localhost:5432/mydb
```

### MySQL
```
mysql://root:password@localhost:3306/mydb
```
