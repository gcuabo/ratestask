# RATES TASK

## Getting Started

### Prerequisites

For ease of setup, using [docker](https://www.docker.com/) is recommended.
If docker is not used, please see the readme without docker setup [here](https://github.com/gcuabo/ratestask/blob/master/README-NO-DOCKER.md)

## Run dev environment

To run dev environment on docker, just do the ff:
```
make dev_up
```

Access the flask app in port 5000
```
curl -v "http://localhost:5000/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"
```

A ping endpoint is available to check the health of the flask app
```
curl "http://localhost:5000/ping"
```

## Kill the dev environment

To spin down dev docker containers:
```
make dev_down
```

## Tests

To run the test from docker containers, just do the ff make command:
```
make run docker_test
```
