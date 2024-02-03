#!/usr/bin/python3
"""
Generates a .tgz archive from web_static folder

"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Packs web_static into a .tgz archive.

    Returns:
        (str): Path of archive if successful, otherwise, none.
    """
    if not os.path.exists("versions"):
        local("mkdir -p versions")

    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.succeeded:
        return archive_path
    else:
        return None


if __name__ == "__main__":
    do_pack()
