#!/bin/bash

kubectl create secret generic steam \
    --from-literal=steam-key="${STEAM_KEY}" \
    --from-literal=steam-id="${STEAM_ID}" \
    --dry-run=client -o yaml |
    kubectl --kubeconfig ~/.kube/bletchley-config -n egroup-bot apply -f -
