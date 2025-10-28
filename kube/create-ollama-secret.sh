#!/bin/bash

kubectl create secret generic ollama \
    --from-literal=ollama-endpoint="${OLLAMA_ENDPOINT}" \
    --from-literal=ollama-llm-model="${OLLAMA_LLM_MODEL}" \
    --dry-run=client -o yaml |
    kubectl --kubeconfig ~/.kube/bletchley-config -n egroup-bot apply -f -
