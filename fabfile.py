#!/usr/bin/python3
""" Fabfile module to compress a folder in .tgz """

from fabric import task
from fabric import Connection
import os.path
from datetime import datetime


@task
def do_pack(c):
    """ Creates a tar gzipped archive of the directory web_static """
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            dt.year,
            dt.month,
            dt.day,
            dt.hour,
            dt.minute,
            dt.second)
    if c.run("test -d versions", warn=True).failed:
        c.run("mkdir -p versions")
    if c.run("tar -cvzf {} web_static".format(file), warn=True).failed:
        return None
    return file
