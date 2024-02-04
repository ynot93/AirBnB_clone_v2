#!/usr/bin/python3
"""
Deletes archives that are out of date

"""

from fabric.api import env, run, local
from datetime import datetime
import os

env.hosts = ['54.87.250.109', '54.90.5.67']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """
    Deletes unnecessary archives from versions and web_static/releases folders

    """
    number = int(number)
    if number < 0:
        return

    local("ls -lt versions | tail -n +{} | awk '{{print $NF}}' | "
          "xargs -I {{}} rm -f versions/{{}}".format(number + 1))
    run("ls -lt /data/web_static/releases | tail -n +{} | "
        "awk '{{print $NF}}' | "
        "xargs -I {{}} rm -rf /data/web_static/releases/{{}}"
        .format(number + 1))


if __name__ == "__main__":
    do_clean(number=2)
