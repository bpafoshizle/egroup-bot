#!/bin/bash

kubectl create secret generic xai \
    --from-literal=xai-api-key="${XAI_API_KEY}" \
    --dry-run=client -o yaml |
    kubectl --kubeconfig ~/.kube/bletchley-config -n egroup-bot apply -f -
