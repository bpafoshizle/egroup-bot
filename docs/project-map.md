# Project Map: egroup-bot

## Overview

This repo is a Discord bot configuration/runner that delegates most bot features to the
local library checkout at `libs/pydiscogs`. The `pydiscogs` library is a separate git
repository and is intended to be iterated on locally while the outer repo provides a
specific bot configuration.

## Top-Level Layout

- `app/` – Bot runtime entrypoint, config, and packaging.
- `libs/pydiscogs/` – Local library repo with cogs, AI tooling, and tests.
- `kube/` – Kubernetes deployment manifests and secret helper scripts.
- `Dockerfile` – Container build that installs app dependencies and runs `app.py`.
- `sensitive/` – Local secrets artifacts (not for committing).

## Runtime Flow

1. `app/app.py` loads `.env`, configures logging, and calls `pydiscogs.botbuilder.build_bot`.
2. `app/egroup-bot.yaml` defines Discord tokens, guild IDs, and the list of enabled cogs.
3. `pydiscogs.botbuilder.build_bot` validates config and registers cogs by name.
4. The bot runs with the token provided in the YAML/env.

Key files:
- `app/app.py`
- `app/egroup-bot.yaml`
- `libs/pydiscogs/src/pydiscogs/botbuilder.py`

## Local `pydiscogs` Install (Primary Dev Loop)

The outer repo is designed to point at the local `libs/pydiscogs` checkout for active
iteration and testing.

- Default dependency (remote): `pydiscogs @ git+https://github.com/bpafoshizle/pydiscogs@main`
  in `app/pyproject.toml`.
- Local override: `tool.uv.sources` points `pydiscogs` at `../libs/pydiscogs` in editable
  mode (`app/pyproject.toml`).
- Container builds use `app/requirements.txt`, which pins a git SHA for reproducibility.

## `pydiscogs` Library Map

### Core Entry

- `libs/pydiscogs/src/pydiscogs/botbuilder.py` – Builds the Discord bot and registers cogs.

### Cogs

- `cogs/ai/` – AI assistant cog using LangGraph + tools + optional Postgres memory.
- `cogs/inspire.py` – Random inspirational quote command.
- `cogs/reddit.py` – Reddit post commands and daily post task.
- `cogs/stocks.py` – Stock quotes/news and daily report task.
- `cogs/twitch.py` – Twitch live checks and user lookup.
- `cogs/wotd.py` – Word of the Day command + daily post task.
- `cogs/news.py` – Placeholder for news support.

### AI Tooling

- `cogs/ai/tools/web_research.py` – Google Search + Gemini research tool.
- `cogs/ai/tools/url_context.py` – URL-context summarization via Gemini.
- `cogs/ai/tools/xai_research.py` – X (Twitter) research via Grok.
- `cogs/ai/tools/read_x_post.py` – Full X post read via API.
- `cogs/ai/tools/computer_control.py` + `playwright_computer.py` – ADK browser automation.
- `cogs/ai/tools/memory_tool.py` – Long-term memory upsert tool.

### Utilities

- `utils/prompts.py` – Prompt templates for research tools.
- `utils/timing.py` – Scheduling helpers for daily tasks.
- `utils/gemini.py` – Gemini citation/url helpers.

### Tests

- `libs/pydiscogs/src/pydiscogs/tests/` – Unit tests for cogs and AI flows.

## Deployment Assets

- `Dockerfile` – Builds a Python 3.13 container and runs `app/app.py`.
- `kube/egroup-bot-deployment.yml` – Kubernetes deployment manifest.
- `kube/create-*-secret.sh` – Secret creation helpers.

## Quick Navigation

- Bot entrypoint: `app/app.py`
- Bot config: `app/egroup-bot.yaml`
- Library root: `libs/pydiscogs/`
- Library cogs: `libs/pydiscogs/src/pydiscogs/cogs/`
- Library tests: `libs/pydiscogs/src/pydiscogs/tests/`
