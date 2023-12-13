# syntax=docker/dockerfile:1
FROM python:3.9.18

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.6.1 \
  POETRY_HOME="/opt/poetry"

RUN pip install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"
ENV PATH=/opt/poetry/bin:$PATH

WORKDIR /code
COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.in-project true && \
    poetry install --no-interaction --no-ansi
ENV PATH=/code/.venv/bin:$PATH

RUN mkdir -p /service/app
COPY app /service/app
RUN mkdir -p /service/src
COPY src /service/src
EXPOSE 8000
COPY docker/start.sh ./
RUN chmod +x start.sh
ENTRYPOINT ["/code/start.sh"]
