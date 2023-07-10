#!/usr/bin/python3
""" Fabfile module to compress a folder in .tgz """

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Creates a tar gzipped archive of the directory web_static """
    dt = datetime.utcnow()
    file = "versions/web_static_{:04d}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz".format(
            dt.year,
            dt.month,
            dt.day,
            dt.hour,
            dt.minute,
            dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
