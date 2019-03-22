# https://docs.docker.com/engine/reference/commandline/network_create/
docker network create \
	--driver=bridge \
	--subnet=172.18.0.0/16 \
	dev
