#!/bin/bash

kubectl create secret generic reddit \
    --from-literal=reddit-username="${REDDIT_USERNAME}" \
    --from-literal=reddit-password="${REDDIT_PASSWORD}" \
    --from-literal=reddit-client-id="${REDDIT_CLIENT_ID}" \
    --from-literal=reddit-client-secret="${REDDIT_CLIENT_SECRET}" \
    --dry-run=client -o yaml |
    kubectl --kubeconfig ~/.kube/bletchley-config -n egroup-bot apply -f -
