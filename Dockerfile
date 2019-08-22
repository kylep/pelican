FROM ubuntu:bionic
Add pelicanconf.py .
Add requirements.txt .
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         python \
         python-pip \
         python-setuptools \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r requirements.txt
