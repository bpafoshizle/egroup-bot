#!/bin/bash

kubectl create secret generic stock \
    --from-literal=polygon-token="${POLYGON_TOKEN}" \
    --from-literal=newsapi-token="${NEWSAPI_TOKEN}" \
    --dry-run=client -o yaml |
    kubectl --kubeconfig ~/.kube/bletchley-config -n egroup-bot apply -f -
