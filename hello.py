#! /usr/bin/env python

from invoke import ctask as task
import subprocess
import sys


@task(help={'message': "String that you want the program to say - default is \"Hello world\""})
def hello(ctx, message=None):
    """Say hello to the user!
    
    Pass the --message flag to say something besides Hello World. You can also
    set the "message" variable in "hello.json"
    """
    if not message:
        message = ctx.config.get('message', None)
    if not message:
        message = "Hello World"
    print(message)


# This boilerplate allows you to use the name of the module for
# the command invocation instead of invoke itself.
if __name__ == "__main__":
    modulename = sys.argv[0].split('/')[-1].split('.')[0]
    configfile = "%s.json"%modulename
    commands = sys.argv[1:] or ['--list']
    args = ['invoke', '-c', modulename, '-f', configfile] + commands
    subprocess.call(args)
