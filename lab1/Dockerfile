FROM python:3.11-slim

WORKDIR /urs/src/app

COPY requirements.txt /urs/src/app/

RUN pip install -r requirements.txt

COPY . /urs/src/app
