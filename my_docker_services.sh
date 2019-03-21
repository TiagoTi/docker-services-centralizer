CURRENT_DIR=''

set_enviroments(){
  . ./docker-compose.env;
  . ./.env;
}

set_pwd_to_temp(){
  CURRENT_DIR=`pwd`;
  cd $MY_DOCKER_SERVICES_DIR;
  set_enviroments
}


# Global config #
set_pwd_to_temp #
# ------------- #


up(){
	docker-compose $dcfiles up -d $1;
}


down(){
	docker-compose $dcfiles rm -sf $1;
}


start(){
	docker-compose $dcfiles start $1;
}


stop(){
	docker-compose $dcfiles stop $1;
}


logs(){
	docker-compose $dcfiles logs -f $1;
}
