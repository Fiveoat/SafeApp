: > ./requirements/requirements.txt
: > ./requirements/requirements-dev.txt

docker_name="safety_app_update_deps"
docker_tag="local"
docker_container="$docker_name:$docker_tag"

docker build -t $docker_container .
docker run -v /$PWD:/opt -it $docker_container /bin/bash /opt/requirements/install_and_freeze.sh
