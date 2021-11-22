# RATES TASK

## Getting Started

### Prerequisites

If docker is not available the app may be setup locally using pipenv
```
pip install pipenv
```

## Run dev environment

To run the app without docker containers (assuming psql is already setup locally):

Install requirements from Pipfile.lock
```
pipenv install --system --deploy --dev
```

Activate pipenv virtualenv
```
pipenv shell
```

run the flask app from the application factory
```
FLASK_APP=core.application:create_flask_app flask run
```

Access the flask app in port 5000
```
curl -v "http://localhost:5000/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"
```


A ping endpoint is available to check the health of the flask app
```
curl "http://localhost:5000/ping"
```


## Tests

To run the tests, just do the ff make command:
```
pytest -v --cov=core/ --cov-report ./tests/
```
