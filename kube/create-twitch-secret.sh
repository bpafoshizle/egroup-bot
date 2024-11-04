#!/bin/bash

kubectl create secret generic twitch \
    --from-literal=twitch-bot-username="${TWITCH_BOT_USERNAME}" \
    --from-literal=twitch-bot-client-id="${TWITCH_BOT_CLIENT_ID}" \
    --from-literal=twitch-bot-client-secret="${TWITCH_BOT_CLIENT_SECRET}" \
    --from-literal=twitch-chat-oauth-token="${TWITCH_CHAT_OAUTH_TOKEN}" \
    --dry-run=client -o yaml | 
    kubectl --kubeconfig ~/.kube/bletchley-config -n egroup-bot apply -f -

