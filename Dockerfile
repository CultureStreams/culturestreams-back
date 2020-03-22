FROM python:3.5-buster

COPY requirements.txt /tmp/

RUN apt-get update && \
    apt-get install -y gcc make libc-dev musl-dev libffi-dev libssl-dev libpcre3-dev && \
    pip install --no-cache-dir -r /tmp/requirements.txt uwsgi && \
    mkdir /code/ && \
    mkdir /data/

COPY ./deployment/docker-entry.sh /
COPY ./culturestreams /code/

EXPOSE 8000

CMD ["/bin/sh", "/docker-entry.sh"]

