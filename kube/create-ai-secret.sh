#!/bin/bash

kubectl create secret generic ai \
    --from-literal=ai-system-prompt="${AI_SYSTEM_PROMPT}" \
    --dry-run=client -o yaml |
    kubectl --kubeconfig ~/.kube/bletchley-config -n egroup-bot apply -f -
