# React Application Boilerplate

Modern React application with best practices and common tools.

## Structure

```
react_app/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   ├── hooks/
│   ├── services/
│   ├── utils/
│   ├── styles/
│   ├── App.js
│   └── index.js
├── .env.example
├── .eslintrc.js
├── .prettierrc
├── package.json
└── README.md
```

## Features

- React 18+
- React Router for navigation
- State management (Context API / Redux Toolkit ready)
- Axios for API calls
- CSS Modules / Styled Components
- ESLint + Prettier
- Environment variables
- Testing with Jest & React Testing Library
- Hot Module Replacement

## Usage

1. Install dependencies: `npm install`
2. Copy `.env.example` to `.env` and configure
3. Run development: `npm start`
4. Build for production: `npm run build`
5. Run tests: `npm test`
6. Lint: `npm run lint`

## Scripts

- `npm start` - Start development server
- `npm run build` - Build for production
- `npm test` - Run tests
- `npm run lint` - Run ESLint
- `npm run format` - Format code with Prettier
