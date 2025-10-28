#!/bin/bash

kubectl create secret generic brave \
    --from-literal=brave-search-api-key="${BRAVE_SEARCH_API_KEY}" \
    --dry-run=client -o yaml |
    kubectl --kubeconfig ~/.kube/bletchley-config -n egroup-bot apply -f -
