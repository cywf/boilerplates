# Python CLI Tool Boilerplate

A production-ready Python CLI application structure using Click or argparse.

## Structure

```
cli_tool/
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── commands/
│   │   ├── __init__.py
│   │   └── example.py
│   └── utils/
├── tests/
├── setup.py
├── requirements.txt
├── README.md
└── .env.example
```

## Features

- Click or argparse for CLI parsing
- Subcommands support
- Configuration management
- Rich output with colors
- Progress bars
- Error handling
- Testing with pytest
- Easy installation via pip

## Usage

### Installation

```bash
# Development mode
pip install -e .

# Or install from requirements
pip install -r requirements.txt
```

### Running

```bash
# Using the installed command
mycli --help
mycli command --option value

# Or run directly
python -m src.cli --help
```

## Commands

- `mycli init` - Initialize configuration
- `mycli run` - Run the main task
- `mycli config` - Manage configuration

## Development

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Run linter
flake8 src/
```
