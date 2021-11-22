FROM python:3.9.9-slim

COPY . /app
WORKDIR /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --dev

ENV DB_HOST db_testing
