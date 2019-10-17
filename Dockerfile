FROM ubuntu:bionic
Add pelicanconf.py requirements.txt .
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         git \
         python \
         python-pip \
         python-setuptools \
         vim \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r requirements.txt \
    && git clone https://github.com/kylep/voidy-bootstrap.git /theme \
    && mkdir -r /tmp-plugins/ /plugins
    && git clone --recurse \
         https://github.com/getpelican/pelican-plugins.git /tmp \
    && cp -r /tmp-plugins/series /plugins/
    && rm -r /tmp-plugins
