#!/bin/python3
from fabric import task
from datetime import datetime

@task
def do_pack():
    """Generates a compressed file"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(file_name))
    return file_name
