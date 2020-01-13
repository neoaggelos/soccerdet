#!/bin/bash

docker-compose run --rm -v "$(realpath ${1}):/tmp/in.yaml:ro" soccerdet import --in /tmp/in.yaml
