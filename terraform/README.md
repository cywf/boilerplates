# Terraform Configuration Templates

Infrastructure as Code templates for common cloud providers.

## Available Templates

- `aws/` - AWS infrastructure templates
- `azure/` - Azure infrastructure templates
- `gcp/` - Google Cloud Platform templates
- `modules/` - Reusable Terraform modules

## Prerequisites

```bash
# Install Terraform
# macOS
brew install terraform

# Or download from https://www.terraform.io/downloads

# Verify installation
terraform version
```

## Usage

```bash
# Initialize Terraform
terraform init

# Format code
terraform fmt

# Validate configuration
terraform validate

# Plan changes
terraform plan

# Apply changes
terraform apply

# Destroy resources
terraform destroy
```

## Best Practices

- Use remote state (S3, Azure Storage, GCS)
- Implement state locking
- Use workspaces for environments
- Create reusable modules
- Use variables and outputs
- Tag all resources
- Implement proper security (IAM, security groups)
- Use data sources for existing resources
- Version pin providers

## Structure

```
terraform/
├── main.tf           # Main configuration
├── variables.tf      # Input variables
├── outputs.tf        # Output values
├── providers.tf      # Provider configuration
├── terraform.tfvars  # Variable values (don't commit secrets)
└── modules/          # Reusable modules
```

## Environment Management

```bash
# Development
terraform workspace new dev
terraform workspace select dev

# Production
terraform workspace new prod
terraform workspace select prod
```
