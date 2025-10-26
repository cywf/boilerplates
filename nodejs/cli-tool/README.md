# Node.js CLI Tool Boilerplate

A modern Node.js CLI application using Commander.js.

## Structure

```
cli_tool/
├── bin/
│   └── cli.js
├── src/
│   ├── commands/
│   │   ├── init.js
│   │   └── run.js
│   └── utils/
│       └── logger.js
├── tests/
├── package.json
├── .env.example
└── README.md
```

## Features

- Commander.js for CLI parsing
- Chalk for colored output
- Inquirer for interactive prompts
- Progress indicators
- Configuration management
- Error handling
- Testing with Jest
- ES6+ modules

## Usage

### Installation

```bash
# Install dependencies
npm install

# Link for local development
npm link

# Or install globally
npm install -g
```

### Running

```bash
# Using the installed command
mycli --help
mycli init
mycli run --option value

# Or run directly
node bin/cli.js --help
```

## Commands

- `mycli init` - Initialize configuration
- `mycli run` - Run the main task
- `mycli config` - Manage configuration

## Development

```bash
# Install dev dependencies
npm install

# Run tests
npm test

# Run linter
npm run lint
```

## Publishing

```bash
# Build (if needed)
npm run build

# Publish to npm
npm publish
```
