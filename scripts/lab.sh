MY_DOCKER_SERVICES_DIR=`pwd`
MY_DOCKER_SERVICES_DIR=$MY_DOCKER_SERVICES_DIR/scripts



if echo $PATH | grep $MY_DOCKER_SERVICES_DIR; then
    echo found
else
    NEW_PATH="export PATH=\$PATH:$MY_DOCKER_SERVICES_DIR"
    echo not found
    echo adding to .bashrc
    echo $NEW_PATH >> $HOME/.bashrc
    echo adding to .zshrc
    echo $NEW_PATH >> $HOME/.zshrc
    echo exporting in this script
    export PATH=$PATH:$MY_DOCKER_SERVICES_DIR
fi
