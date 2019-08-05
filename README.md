# All Services One Repo

```
export VANELLOPE_SRC=/home/tiago/projetos/vanellope
export VANELLOPE_MOCK_SRC=/home/tiago/projetos/resupply-frontend-pitaco-python-mock-server
```

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
version: "3.7"

services:
  ubuntu:
    build:
      context: build/context/ubuntu
    container_name: ubuntu
    tty: true
```

Add new entry in `docker-compose.env` with you new docker file name
`-f $MY_DOCKER_SERVICES_DIR/docker-compose-ubuntu.yaml \`

---
## Install 

```sh
#make a folder to put script
mkdir -p $HOME/bin

#make dowload from bin
curl -L https://github.com/TiagoTi/gitchu/releases/download/v0.0.0/container.py -o $HOME/bin/container && chmod +x $HOME/bin/container

#add folder to path if necessary
export PATH=$PATH:$HOME/bin

## Use
container start redis

### Create a new lan
container newlan 172.18.0.0/16 dev
```