# GitHub Actions CI/CD Templates

Collection of GitHub Actions workflow templates for various use cases.

## Available Workflows

### Basic Workflows
- `node-ci.yml` - Node.js CI/CD pipeline
- `python-ci.yml` - Python CI/CD pipeline
- `docker-build.yml` - Docker build and push
- `terraform.yml` - Terraform infrastructure deployment

### Advanced Workflows
- `release.yml` - Automated releases
- `security-scan.yml` - Security scanning
- `test-coverage.yml` - Code coverage reporting

## Usage

1. Copy the desired workflow file to `.github/workflows/`
2. Customize variables and secrets
3. Push to GitHub to trigger the workflow

## Required Secrets

Common secrets you may need to configure:
- `DOCKER_USERNAME` - Docker Hub username
- `DOCKER_PASSWORD` - Docker Hub password or token
- `AWS_ACCESS_KEY_ID` - AWS access key
- `AWS_SECRET_ACCESS_KEY` - AWS secret key
- `SLACK_WEBHOOK` - Slack notification webhook

## Best Practices

- Use caching for dependencies
- Run jobs in parallel when possible
- Use matrix builds for multiple versions
- Implement proper error handling
- Add notifications for failures
