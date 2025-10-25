# Kubernetes Manifests

Collection of Kubernetes resource templates for common deployment scenarios.

## Available Templates

- `deployment.yml` - Basic application deployment
- `service.yml` - Service definitions (ClusterIP, NodePort, LoadBalancer)
- `ingress.yml` - Ingress configuration
- `configmap.yml` - Configuration management
- `secret.yml` - Secret management
- `statefulset.yml` - StatefulSet for databases
- `job.yml` - Job and CronJob templates
- `namespace.yml` - Namespace configuration

## Usage

```bash
# Apply a single manifest
kubectl apply -f deployment.yml

# Apply all manifests in directory
kubectl apply -f .

# Dry run to validate
kubectl apply -f deployment.yml --dry-run=client

# Delete resources
kubectl delete -f deployment.yml
```

## Best Practices

- Use namespaces for isolation
- Set resource limits and requests
- Implement health checks (liveness/readiness probes)
- Use ConfigMaps and Secrets for configuration
- Implement proper labels and selectors
- Use rolling updates for deployments
- Set up proper RBAC

## Customization

1. Replace placeholder values (e.g., `myapp`, `your-image:tag`)
2. Adjust resource limits based on your needs
3. Configure environment variables
4. Set up proper labels and annotations
5. Configure ingress based on your provider
