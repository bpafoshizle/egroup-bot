#!/bin/bash

kubectl --kubeconfig ~/.kube/bletchley-config \
    -n egroup-bot \
    create secret docker-registry ghcr-egroup-bot \
    --docker-server=ghcr.io \
    --docker-username="${GITHUB_USERNAME}" \
    --docker-password="${GITHUB_PACKAGE_TOKEN}"  \
    --docker-email="${GITHUB_EMAIL}"
