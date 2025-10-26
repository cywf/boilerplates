# Configuration Files

Collection of configuration files for common development tools.

## Available Configurations

### Code Quality
- `eslint/` - ESLint configurations for various projects
- `prettier/` - Prettier formatting configurations
- `editorconfig/` - EditorConfig for consistent coding styles

### Linters & Formatters
- `.eslintrc.js` - JavaScript/TypeScript linting
- `.prettierrc` - Code formatting
- `.editorconfig` - Editor settings
- `.pylintrc` - Python linting
- `pyproject.toml` - Python project configuration

## Usage

1. Copy the desired configuration file to your project root
2. Customize settings as needed
3. Install required dependencies
4. Run linter/formatter

## Tool-specific Setup

### ESLint
```bash
npm install --save-dev eslint
npx eslint --init
```

### Prettier
```bash
npm install --save-dev prettier
npx prettier --write .
```

### Black (Python)
```bash
pip install black
black .
```
