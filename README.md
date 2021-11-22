# RATES TASK

## Run dev environment

### With Docker

To run dev environment on docker, just do the ff:
```
make dev_up
```

Access the flask app in port 5000
```
curl "http://localhost:5000/ping"
```

### Without docker containers

To run the app without docker containers (assuming psql is already setup locally):

Install pipenv:
```
pip install pipenv
```

Install requirements from Pipfile.lock
```
pipenv install --system --deploy --dev
```

run the flask app from the application factory
```
FLASK_APP=core.application:create_flask_app flask run
```

## Tests

to run the test from docker containers, just do the ff make command:
```
make run docker_test
```
