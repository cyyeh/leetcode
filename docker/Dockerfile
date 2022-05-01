FROM python:3.8-slim

# https://stackoverflow.com/a/57414078
ENV PYTHONPYCACHEPREFIX=/.cache

RUN apt update -y && apt install make

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . /code
