#!/bin/bash

# Read all non-commented lines from the .env file in the parent directory,
# then export them as environment variables for this script and its children.
set -o allexport
if [ -f ../.env ]; then
  # shellcheck disable=SC1091
  source ../.env
fi
set +o allexport

./create-discord-token-secret.sh
./create-gfycat-secret.sh
./create-ghcr-secret.sh
./create-namespace.sh
./create-reddit-secret.sh
./create-stock-secrets.sh
./create-twitch-secret.sh
./create-ollama-secret.sh
./create-google-secret.sh
./create-groq-secret.sh
./create-brave-secret.sh
./create-steam-secret.sh
./create-ai-secret.sh