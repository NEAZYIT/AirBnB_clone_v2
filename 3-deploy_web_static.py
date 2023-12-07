#!/usr/bin/python3
"""
This script creates and distributes an archive to web servers using Fabric.
The archive is created using the do_pack() function and then deployed to
the servers using the do_deploy() function.
"""

from fabric.api import env, local, run
from os.path import exists
from datetime import datetime

env.hosts = ['100.26.243.102', '54.237.96.116']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """

    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Create a timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Create the archive
    local("tar -cvzf versions/web_static_{}.tgz web_static".format(timestamp))

    # Return the archive path if the file was created
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    return archive_path if exists(archive_path) else None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not exists(archive_path):
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as e:
        return False


def deploy():
    """
    Deploys archive to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
