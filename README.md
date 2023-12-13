# Mistral Playground

Simple playground wrapper around Mistral API.

## Installation Guide

The project can be launched in three different setups: with a local app, inside a Docker image and on an Azure Webapp.

### Local API


The project dependencies are managed using `poetry`, see their installation [guide](https://python-poetry.org/docs/). For even more stability, I recommend using `pyenv` or python `3.9.18`.

Additionally, to make your life easier, install `make` to use the shortcut commands.

#### Base Install

To install the dependencies:

```bash
poetry install
```

To launch the app:

```bash
make appstart
```

#### Dev Install

To install the dependencies:

```bash
poetry install --with dev
```

Before committing, install `pre-commit`:

```bash
pre-commit install
```

To run the checks (`pre-commit` checks):

```bash
make checks
```

To run the tests (using `pytest`):

```bash
make tests
```

### Docker

See Docker install [guide](https://docs.docker.com/engine/install/).

To launch the image:

```bash
make start
```

To (re)build the image:

```bash
make build
```

To deploy the image (run in the background and rebuild automatically):

```bash
make deploy
```

To stop a deployed image:

```bash
make stop
```

To obtain a tty in a deployed image:

```bash
make tty
```
