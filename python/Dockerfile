# Build
FROM python:3.11-slim AS build

RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv --copies /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel

# Build the virtualenv as a separate step: Only re-execute this step when requirements.txt changes
FROM build AS build-venv

COPY requirements.txt /requirements.txt

ENV PATH="venv/bin:$PATH"

RUN pip install -r /requirements.txt

# Final stage

FROM python:3.11-slim

COPY --from=build-venv /venv /venv
COPY . /app

WORKDIR /app

EXPOSE 8000

ENV PATH="/venv/bin:$PATH"

CMD ["python3", "api.py"]
