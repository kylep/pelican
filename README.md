# Pelican Docker Image

Used for generating my
[blog content](https://github.com/kylep/kyle.pericak.com).

You can find the blog [here](https://kyle.pericak.com).

# Build Local Image
For the dev environment
```bash
./local-build.sh
```

# Manually upload image to GCP's GCR
I've got a Trigger in GCP Cloud Builder to do this every git push.
To manually update the image without pushing to GitHub, run:
```bash
./gcp-build.sh
```

# Upload to Docker Hub
I like to share the image here too in case anyone else wants to play with it.
Its hosted on Google's container registry but I don't want to pay for public
access.
```bash
./docker-hub-build.sh
```
