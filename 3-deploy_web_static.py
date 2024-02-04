#!/usr/bin/python3
"""
Distributes the archive to web servers

"""

from fabric.api import local, env, run, put
from datetime import datetime
import os

env.hosts = ['54.87.250.109', '54.90.5.67']


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


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        bool: True if all operations are correct correctly, otherwise False.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[1]
        version = file_name.split('.')[0]

        put(archive_path, '/tmp/{}'.format(file_name))
        run('mkdir -p /data/web_static/releases/{}/'.format(version))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file_name, version))

        run('rm /tmp/{}'.format(file_name))

        run(('mv /data/web_static/releases/{}/web_static/* '
             '/data/web_static/releases/{}/').format(version, version))

        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(version))

        run('rm -rf /data/web_static/current')

        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(version))

        print('New version deployed!')
        return True

    except Exception as e:
        print(e)
        return False


def deploy():
    """
    Calss do_pack and do_deploy

    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)


if __name__ == "__main__":
    archive_path = 'versions/web_static_20240202021833.tgz'
    deploy()
