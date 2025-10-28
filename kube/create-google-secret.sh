#!/bin/bash

kubectl create secret generic google \
    --from-literal=gemini-api-key="${GEMINI_API_KEY}" \
    --from-literal=google-api-key="${GOOGLE_API_KEY}" \
    --from-literal=google-llm-model="${GOOGLE_LLM_MODEL}" \
    --dry-run=client -o yaml |
    kubectl --kubeconfig ~/.kube/bletchley-config -n egroup-bot apply -f -
