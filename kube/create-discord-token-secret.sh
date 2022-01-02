#!/bin/bash

kubectl create secret generic discord \
    --from-literal=token="${DISCORD_PROD_TOKEN}" \
    --from-literal=dscrd-chnl-bot-testing="${DSCRD_PROD_CHNL_BOT_TESTING}" \
    --from-literal=dscrd-chnl-general="${DSCRD_PROD_CHNL_GENERAL}" \
    --from-literal=dscrd-chnl-meal-pics="${DSCRD_PROD_CHNL_MEAL_PICS}" \
    --from-literal=dscrd-chnl-sports="${DSCRD_PROD_CHNL_SPORTS}" \
    --from-literal=dscrd-chnl-politics="${DSCRD_PROD_CHNL_POLITICS}" \
    --from-literal=dscrd-chnl-money="${DSCRD_PROD_CHNL_MONEY}" \
    --from-literal=dscrd-chnl-gaming="${DSCRD_PROD_CHNL_GAMING}" \
    --from-literal=dscrd-chnl-bot-feature-requests="${DSCRD_PROD_CHNL_BOT_FEATURE_REQUESTS}" \
    --from-literal=dscrd-guild-id="${DISCORD_EGROUP_GUILD_ID}" \
    --dry-run=client -o yaml \
    | kubectl --kubeconfig ~/.kube/bletchley-config -n egroup-bot apply -f -

