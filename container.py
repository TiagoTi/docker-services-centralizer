#!python
import sys
import os
import argparse
import glob

NAME="services"
PATH="/mnt/hd_um_tera/tiago/services"
PROJECT_DIRECTORY = f" --project-directory {PATH} "
PROJECT_NAME = f" --project-name {NAME} "
DOCKER_COMPOSE = f"docker-compose {PROJECT_DIRECTORY} {PROJECT_NAME} --file "

def run_linux_command(command):
    print(command)
    os.system(command)

def grouping_files():
    files_ = []
    files = [f for f in glob.glob(PATH + "**/*.yaml", recursive=True)]
    files = " --file ".join(files)
    return files

def docker_compose():
    parser = argparse.ArgumentParser()
    parser.add_argument('command',help= 'A basic command to your container like: up , down, start, stop, create')
    parser.add_argument('commons_args', nargs='*')
    args = parser.parse_args()

    if args.command:
        command = ""
        if args.command == "start":
            print("starting services")
            command = f'{DOCKER_COMPOSE} {grouping_files()} start {" ".join(args.commons_args)}'
            
        if args.command == "up":
            print("up services")
            command = f'{DOCKER_COMPOSE} {grouping_files()} up -d {" ".join(args.commons_args)}'

        if args.command == "stop":
            print("stops services")
            command = f'{DOCKER_COMPOSE} {grouping_files()} stop {" ".join(args.commons_args)}'

        if args.command == "newlan":
            print("ok vamos criar uma lan")
            command = f"docker network create --driver=bridge --subnet={args.commons_args[0]} {args.commons_args[1]}"
            
        run_linux_command(command)


if __name__ == '__main__':
    docker_compose()
