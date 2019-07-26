# All Services One Repo

## Config path
echo "export MY_DOCKER_SERVICES_DIR=`pwd`" >> ~/.bashrc
echo "export PATH=$PATH:$MY_DOCKER_SERVICES_DIR/scripts" >> ~/.bashrc

`reopen terminal`

## [Install Docker Compose](https://docs.docker.com/compose/install/)
Verify min version from compose to docker-file.yml 3.7


## Obtain `.env` to use docker created based in personal projects

---

# Add a new docker to stack

Create a new file to builded image (in this sample I will create a ubuntu docker)

`touch $MY_DOCKER_SERVICES_DIR/docker-compose-ubuntu.yaml`

Chose de verson of file: `3.7`  
Add a service name `ubuntu`  
Aad dir from Dockerfile `build/context/ubuntu` in context  
Define a Container Name: `container_name: mkdocs`  

## The final sample is like:

```yaml
version: "3.3"

services:
  ubuntu:
    build:
      context: build/context/ubuntu
    container_name: ubuntu
    tty: true
```

Add new entry in `docker-compose.env` with you new docker file name
`-f $MY_DOCKER_SERVICES_DIR/docker-compose-ubuntu.yaml \`

