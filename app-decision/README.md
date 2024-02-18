Decision App
============

Simple Mock Application exposing a REST endpoint that randomly returns a decision string from a list of predefined items.

# Usage

To run the app locally, use [poetry](https://python-poetry.org/) to install dependencies and set up the environment

To start the app for local development, run:

```
poetry run python app.py
```

To execute tests, run:

```
poetry run pytest
```

# Build

For deployment, the application is packaged inside a docker container.

To build the container, run 

```bash
docker build -t ggrab/appdecision:latest .
```

To then publish the container to DockerHub, run 

```bash
docker push ggrab/appdecision:latest .
```
