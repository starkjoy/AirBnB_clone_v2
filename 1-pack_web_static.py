#!/usr/bin/python3
""" Fabfile module to compress a folder in .tgz """

from fabric import task
from fabric import Connection
import os.path
from datetime import datetime


@task
def do_pack():
    """ Creates a tar gzipped archive of the directory web_static """
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            dt.year,
            dt.month,
            dt.hour,
            dt.minute,
            dt.second)
    if run("test -d versions", warn=True).failed:
        run("mkdir -p versions")
    if run("tar -cvzf {} web_static".format(file), warn=True).failed:
        return None
    return file
