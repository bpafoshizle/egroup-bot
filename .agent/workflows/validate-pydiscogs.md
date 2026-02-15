---
description: Run tests and linting for the pydiscogs library
---

# Validate pydiscogs

This workflow runs the test suite and performs linting using black, flake8, and isort within the `libs/pydiscogs` directory.

## Steps

1. **Enter directory**
   ```bash
   cd libs/pydiscogs
   ```

// turbo
2. **Run Tests**
   Run the unittest suite using the virtual environment's python.
   ```bash
   ./.venv/bin/python3 -m unittest discover src
   ```

// turbo
3. **Format Check (isort)**
   Check import ordering.
   ```bash
   ./.venv/bin/isort --check src
   ```

// turbo
4. **Format Check (black)**
   Check code formatting.
   ```bash
   ./.venv/bin/black --check src
   ```

// turbo
5. **Linting (flake8)**
   Check for style guide enforcements.
   ```bash
   ./.venv/bin/flake8 src
   ```
