# AM Flow API experiment

## Setup

- Copy the .env.template file to .env and edit the configuration

- In a virtualenv, install poetry

```bash
pip install poetry
```

- Install dependencies with poetry

```bash
poetry install
```

## Launch the webhook

```bash
poetry run python webhook.py
```

## Launch the script

```bash
poetry run python main.py
```
