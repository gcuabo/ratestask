FROM python:3.9.9-slim

COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy --dev
