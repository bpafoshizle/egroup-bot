#!/bin/bash

kubectl create secret generic groq \
    --from-literal=groq-api-key="${GROQ_API_KEY}" \
    --from-literal=groq-llm-model="${GROQ_LLM_MODEL}" \
    --dry-run=client -o yaml |
    kubectl --kubeconfig ~/.kube/bletchley-config -n egroup-bot apply -f -
