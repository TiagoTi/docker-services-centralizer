# Today

Durantes as minhas primeiras tentativas de gerar o novo processo de integração
continua usando o gitlab-runner, eu não havia entendido que para rodar localmente,
todas as variaveis que ficam online devem ser envidas com o comando --env.

## variaveis terry terri

No terry-terry vamos precisar de authenticar no pip para isso precisamos:

`warning` `c.i online` `test` PYPI_USERNAME, PYPI_PASSWORD são usadas apenas para teste.

`warning` `c.i tools` `prod | stage` ENVIROMENT  
é setado dentro do job ele determina como o makefile vai regir

`warning` `c.i tools` `global` TERESA_CLUSTER_NAME
essa eu abstrai o clustername é irrelevante para uma máquina efemera que só usamos para deploy

`warning` `c.i tools | online` `prod | stage` TERESA_CLUSTER_URL: $(TERESA_CLUSTER_URL_PRD)
essa aqui terá duas versões que são identificadas no job de stage e de prod

```
gitlab-runner exec docker \
		--env PYPI_USERNAME=${PYPI_USERNAME} \
		--env PYPI_PASSWORD=${PYPI_PASSWORD} \
		--env TERESA_USER=${TERESA_USER} \
		--env TERESA_PASSWORD=${TERESA_PASSWORD} \
		--env TERESA_CLUSTER_URL=${TERESA_CLUSTER_URL_STAGE} \
		--env TERESA_CLUSTER_URL_STAGE=${TERESA_CLUSTER_URL_STAGE} \
		deploy_stage_terri
```
