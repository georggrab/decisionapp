FROM python:3.11 AS builder

# Don't buffer stdout
ENV PYTHONUNBUFFERED=1 

# Don't create `.pyc` files:
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install poetry && poetry config virtualenvs.in-project true

WORKDIR /app

COPY . .
RUN poetry install --no-root --without dev

FROM python:3.11-alpine
WORKDIR /app

COPY --from=builder /app .

RUN adduser app -DHh ${WORKDIR} -u 1000
USER 1000

# App-specific settings:
EXPOSE 8080
CMD ["/app/.venv/bin/gunicorn", "--bind", ":8080", "app:create_app()"]
