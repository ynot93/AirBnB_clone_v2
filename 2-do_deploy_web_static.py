#!/usr/bin/python3
"""
Distributes an archive to web servers using do_deploy.

"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.87.250.109', '54.90.5.67']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        bool: True if all operations are correct correctly, otherwise False.
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        file_no_ext = archive_path.split('/')[-1].split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(file_no_ext))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
            .format(file_no_ext, file_no_ext))

        run('rm /tmp/{}.tgz'.format(file_no_ext))

        run(('mv /data/web_static/releases/{}/web_static/* '
             '/data/web_static/releases/{}/').format(file_no_ext, file_no_ext))

        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(file_no_ext))

        run('rm -rf /data/web_static/current')

        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(file_no_ext))

        print('New version deployed!')
        return True

    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    archive_path = 'versions/web_static_20240202021833.tgz'
    do_deploy(archive_path)
