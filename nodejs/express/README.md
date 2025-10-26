# Express.js Application Boilerplate

A production-ready Express.js REST API structure.

## Structure

```
express_app/
├── src/
│   ├── controllers/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── config/
│   └── app.js
├── tests/
├── .env.example
├── .eslintrc.js
├── .prettierrc
├── package.json
└── README.md
```

## Features

- ES6+ with ESM modules
- RESTful API structure
- Middleware support
- Error handling
- Environment configuration
- Database integration ready
- Logging with Winston
- Input validation
- Security headers (Helmet)
- Rate limiting
- CORS enabled

## Usage

1. Install dependencies: `npm install`
2. Copy `.env.example` to `.env` and configure
3. Run development: `npm run dev`
4. Run production: `npm start`
5. Run tests: `npm test`
6. Lint: `npm run lint`

## Endpoints

- `GET /api/health` - Health check
- `GET /api/v1/users` - Get all users (example)
