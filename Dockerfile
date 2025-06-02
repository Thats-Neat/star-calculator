FROM python:3.11-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    PYTHONBUFFERED=1

RUN apt-get update 

WORKDIR /home/workspace

COPY . .

RUN pip install .
