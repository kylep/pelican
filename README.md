# Pelican Docker Image

Used for generating my blog content. Blog source files are
[here](https://github.com/kylep/kyle.pericak.com).

The blog itslef is [here](https://kyle.pericak.com).

Feel free to use this image, I've shared it on
[Docker Hub](https://cloud.docker.com/u/kpericak/repository/docker/kpericak/pelican).


# Dev Scripts
There are a few scripts in `bin/` to make working on this easier. They're meant
to be ran from the project root.

## Manually upload image to GCP's GCR
```bash
bin/gcp-build.sh
```

## Upload to Docker Hub
I don't want to pay for any public downloads from GCR so I share it on Docker
Hub using this command:
```bash
bin/docker-hub-build.sh
```

## Local Docker Build
Subset of the Docker Hub command, this builds the local image but doesn't
upload it anywhere.
