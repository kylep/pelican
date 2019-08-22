#!/usr/bin/env bash

tag="latest"
if [[ ! -z $1 ]]; then
  tag=$1
fi

docker login
docker build -t kpericak/pelican:$tag .
docker push kpericak/pelican:$tag
