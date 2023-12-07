#!/usr/bin/python3
"""
This script deletes out-of-date archives from the web servers.
"""

from fabric.api import run, env
from os import listdir, path
env.hosts = ['100.26.243.102', '54.237.96.116']


def do_clean(number=0):
    """Delete out-of-date archives"""
    number = int(number)

    # keep at least one archive if number <= 1
    if number <= 1:
        number = 2
    else:
        number += 1

    local('ls -dt versions/* | tail -n +{} | xargs rm -rf --'.format(number))
    cmd = 'ls -dt /data/web_static/releases/* | tail -n +{} | xargs rm -rf --'
    run(cmd.format(number))
