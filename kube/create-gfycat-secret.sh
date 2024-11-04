#!/bin/bash

kubectl create secret generic gfycat \
    --from-literal=gfycat-client-id="${GFYCAT_CLIENT_ID}" \
    --from-literal=gfycat-client-secret="${GFYCAT_CLIENT_SECRET}" \
    --dry-run=client -o yaml |
    kubectl --kubeconfig ~/.kube/bletchley-config -n egroup-bot apply -f -
