#!/bin/bash

kubectl create secret generic ai \
    --from-literal=ai-system-prompt="${AI_SYSTEM_PROMPT}" \
    --from-literal=postgres-db-prod-url="${POSTGRES_DB_PROD_URL}" \
    --dry-run=client -o yaml |
    kubectl --kubeconfig ~/.kube/bletchley-config -n egroup-bot apply -f -
