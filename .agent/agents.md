# AI Agents and Architecture

This document tracks the technical details and operational guides for the AI components of the **egroup-bot**.

## Overview
The bot uses an agentic architecture built on **LangGraph**. The primary unit of AI logic is the **AI Cog** located in `libs/pydiscogs`.

## AI Infrastructure
- **Framework**: LangGraph
- **Base LLM**: Supports Google Gemini, Groq, and Ollama (configurable via `egroup-bot.yaml`).
- **Persistence**: Postgres-backed checkpoints via `AsyncPostgresSaver`.
- **Memory**:
  - **Short-term**: Per-channel/thread conversation persistence.
  - **Long-term**: Planned summarization and cross-thread fact storage using LangGraph's `Store`.

## Development Workflows

### Local Testing with Editable Libs
To test changes in `libs/pydiscogs` directly from the `app` runner:
1. Uncomment the following in `app/pyproject.toml` (it is commented out by default for production):
   ```toml
   [tool.uv.sources]
   pydiscogs = { path = "../libs/pydiscogs", editable = true }
   ```
2. Run `uv sync` from the `app` directory.

### Postgres Memory
The bot requires a Postgres database for conversation memory.
- **Env Var**: `POSTGRES_DB_URL` (mapped from `POSTGRES_DB_PROD_URL` secret in production)
- **Tables**: `checkpoints` and `checkpoint_blobs` are automatically created on first use.
