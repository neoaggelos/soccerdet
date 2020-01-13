#!/bin/bash

ADMIN_PASSWORD="${1}"

docker-compose run --rm soccerdet migrate
docker-compose run --rm soccerdet createadmin --username admin --password "${ADMIN_PASSWORD}" --noinput --email admin@localhost

docker-compose up -d
