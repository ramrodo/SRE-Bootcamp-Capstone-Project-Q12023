# ramrodo/academy-sre-bootcamp-rodolfo-martinez
# Build
FROM python:3.11-slim AS build

RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv --copies /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel

# Build the virtualenv as a separate step: Only re-execute this step when requirements.txt changes
FROM build AS build-venv

COPY capstone-api/requirements.txt /requirements.txt

ENV PATH="venv/bin:$PATH"

RUN pip install -r /requirements.txt

# Final stage

FROM python:3.11-slim@sha256:d0e839882b87135b355361efeb9e9030c9d2a808da06434f4c99eb4009c15e64

COPY --from=build-venv /venv /venv
COPY capstone-api /capstone-api

WORKDIR /capstone-api

EXPOSE 80

ENV PATH="/venv/bin:$PATH"

CMD [ "gunicorn", "--bind", "0.0.0.0:80", "wsgi:app" ]

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost:80/_health
