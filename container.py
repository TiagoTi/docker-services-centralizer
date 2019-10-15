#!python3
import sys
import os
import argparse
import glob
from dotenv import load_dotenv
load_dotenv()


NAME=os.getenv('DOCKER_SERVICES_CENTRALIZER_NAME')
PATH=os.getenv('DOCKER_SERVICES_CENTRALIZER_PATH')
DOCKER_COMPOSE_BIN=os.getenv('DOCKER_SERVICES_CENTRALIZER_PATH_BIN', 'docker-compose')
PROJECT_DIRECTORY = f" --project-directory {PATH} "
PROJECT_NAME = f" --project-name {NAME} "
DOCKER_COMPOSE = f"{DOCKER_COMPOSE_BIN} {PROJECT_DIRECTORY} {PROJECT_NAME} --file "


def run_linux_command(command):
    os.system(command)


def grouping_files():
    files = [f for f in glob.glob(PATH + "**/*.yaml", recursive=True)]
    return " --file ".join(files)


def docker_compose():
    parser = argparse.ArgumentParser()
    parser.add_argument('command',help= 'A basic command to your container like: up , down, start, stop, create')
    parser.add_argument('commons_args', nargs='*')
    args = parser.parse_args()
    command = "pwd"

    if args.command:
        commands =  {
            "start": f'{DOCKER_COMPOSE} {grouping_files()} start {" ".join(args.commons_args)}',
            "stop": f'{DOCKER_COMPOSE} {grouping_files()} stop {" ".join(args.commons_args)}',
            "up": f'{DOCKER_COMPOSE} {grouping_files()} --compatibility up -d {" ".join(args.commons_args)}',
            "down": f'{DOCKER_COMPOSE} {grouping_files()} down {" ".join(args.commons_args)}',
            "build": f'{DOCKER_COMPOSE} {grouping_files()} build --force-rm  {" ".join(args.commons_args)}',
        }

        if args.command in commands.keys():
            command = commands[args.command]

        if args.command == "newlan":
            command = f"docker network create --driver=bridge --subnet={args.commons_args[0]} {args.commons_args[1]}"
    run_linux_command(command)


if __name__ == '__main__':
    docker_compose()
