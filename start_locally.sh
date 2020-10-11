#!/usr/bin/env bash
docker_name="safety_app"
docker_tag="local"
docker_container="$docker_name:$docker_tag"

docker build --build-arg DEV=true -t $docker_container .
docker run -v /$PWD:/opt -i -t $docker_container /bin/bash
