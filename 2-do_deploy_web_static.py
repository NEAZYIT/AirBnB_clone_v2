#!/usr/bin/python3
"""
This script uses Fabric to distribute an archive to web servers.
The archive is uploaded to the /tmp/ directory of the web server,
uncompressed to the folder
/data/web_static/releases/<archive filename without extension>,
and the symbolic link /data/web_static/current
is updated to point to this folder.
All remote commands are executed on both web servers.
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['100.26.243.102', '54.237.96.116']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
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
    except:
        return False
