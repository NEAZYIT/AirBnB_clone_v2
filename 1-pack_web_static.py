#!/usr/bin/python3
"""
This script uses Fabric to generate a .tgz archive from the contents of the
web_static folder. The archive is stored in the versions folder with a name
formatted as web_static_<year><month><day><hour><minute><second>.tgz.

The script creates the necessary directories if they don't exist, creates the
archive, and returns the archive path if the archive has been correctly
generated. Otherwise, it returns None.
"""
from fabric.api import local
from datetime import datetime


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
    try:
        with open(archive_path):
            return archive_path
    except IOError:
        return None
