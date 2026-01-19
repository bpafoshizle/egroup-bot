# Configuration Workflow

This document outlines the steps required to add new configuration settings (like API keys, database URLs, etc.) to the egroup-bot.

## 1. Secrets Management

If the configuration involves sensitive data (API keys, passwords, database URLs), do **not** commit them directly to variables or YAML files.

### 1.1. Add to Kubernetes Secrets
Edit the appropriate secret creation script in the `kube/` directory (e.g., `kube/create-ai-secret.sh`, `kube/create-stock-secret.sh`, etc.).

Add a new line to map an environment variable to a secret key:

```bash
kubectl create secret generic actions \
    ...
    --from-literal=new-secret-key="${NEW_SECRET_ENV_VAR}" \
    ...
```

### 1.2. Verify Secret Creation
Run the script with `--dry-run=client` to ensure the YAML is generated correctly without applying it:

```bash
export NEW_SECRET_ENV_VAR="test-value"
./kube/create-ai-secret.sh --dry-run=client
```

## 2. Deployment Manifest

Update the Kubernetes deployment manifest to expose the secret to the application container as an environment variable.

### 2.1. Edit `kube/egroup-bot-deployment.yml`
Locate the `env` section of the `egroup-bot` container and add a new entry:

```yaml
        - name: NEW_CONFIG_NAME
          valueFrom:
            secretKeyRef:
              name: secret-name  # The name of the secret (e.g., 'ai', 'stock')
              key: new-secret-key # The key you used in step 1.1
```

## 3. Application usage

The configuration will now be available as an environment variable in the application runtime.

### 3.1. Python Code
Access the variable using `os.environ` or `os.getenv`:

```python
import os
config_value = os.getenv("NEW_CONFIG_NAME")
```

## 4. Local Development

For local development where you might not be running Kubernetes:

1. Ensure you have the environment variable set in your `.env` file or shell environment.
2. If using `app/pyproject.toml` overrides for local library development, ensure `pydiscogs` is pointed to your local checkout.

```toml
# app/pyproject.toml
[tool.uv.sources]
pydiscogs = { path = "../libs/pydiscogs", editable = true }
```
