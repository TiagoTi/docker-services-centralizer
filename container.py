#!python
import sys
import os
import argparse


def run_linux_command(command):
    print(command)
    os.system(command)


def docker_compose():
    parser = argparse.ArgumentParser()
    parser.add_argument('command',help= 'A basic command to your container like: up , down, start, stop, create')
    parser.add_argument('commons_args', nargs='*')
    args = parser.parse_args()


    if args.command:
        if args.command == "newlan":
            print("ok vamos criar uma lan")
            command = f"docker network create --driver=bridge --subnet={args.commons_args[0]} {args.commons_args[1]}"
            run_linux_command(command)


if __name__ == '__main__':
    docker_compose()
