FROM python:3.9.9-slim

COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy --dev

ENV FLASK_APP=core.application:create_flask_app
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
