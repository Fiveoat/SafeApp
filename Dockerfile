FROM python@sha256:1a126607adde46a706e76357c910f36b9f5529fb575d4d86a639a4997daceba7

ARG USER_ID=1000
ARG GROUP_ID=1000

RUN addgroup --gid $GROUP_ID default_group
RUN adduser --gecos '' --disabled-password --uid $USER_ID --gid $GROUP_ID  default
USER default

WORKDIR /opt
ENV PYTHONPATH $PYTHONPATH:/opt:/home/default/.local/bin
ENV PATH $PATH:/home/default/.local/bin

COPY ["./requirements/requirements.txt", "./requirements/requirements.txt"]
RUN pip --use-feature=2020-resolver install --user -r ./requirements/requirements.txt

ARG DEV=false
ENV DEV="${DEV}"

COPY ["./requirements/requirements-dev.txt", "./requirements/requirements-dev.txt"]
COPY ["./requirements/install_dev_requirements.sh", "./requirements/install_dev_requirements.sh"]
RUN bash ./requirements/install_dev_requirements.sh
RUN pip check

ARG ENVIRONMENT=local
ARG DEBUG=false

ENV ENVIRONMENT="${ENVIRONMENT}"
ENV DEBUG="${DEBUG}"

ADD . /opt

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
CMD ["python", "python_docker_example/main.py"]
