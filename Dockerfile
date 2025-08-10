FROM python:3.12-alpine

RUN pip install --no-cache-dir "https://github.com/agorf/fit2gpx/archive/refs/heads/main.zip"

# Create a non-root user and a writable workspace
RUN adduser -D -h /work app
WORKDIR /work
USER app

ENTRYPOINT ["fit2gpx"]
