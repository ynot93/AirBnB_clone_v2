#!/usr/bin/python3
"""
Deletes archives that are out of date

"""

from fabric.api import *
import os

env.hosts = ['54.87.250.109', '54.90.5.67']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """
    Deletes unnecessary archives from versions and web_static/releases folders

    """
    if int(number) == 0:
        number = 1
    else:
        int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
