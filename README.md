# Essential Python

## pip

### install poetry (if you don't have it already)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### execute

poetry install
poetry run python postgresql.py

## Langfuse 

### Overview

https://langfuse.com/docs

### Interactive Demo

https://langfuse.com/docs/demo

## Create Environment

```bash
docker compose up -d
```

### Logs

```bash
docker compose logs -f
```

```bash
docker compose down --remove-orphans