#!/usr/bin/python3
"""Fabfile to create and distribute an archive to a web server"""

import os.path
from fabric.api import env, put, run

env.hosts = ["52.207.78.146", "35.175.64.54"]
archive_path = "versions/*"

def do_deploy(archive_path):
    """Distributes an archive to a web server

    Args:
        archive_path (str): The path of archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False
        Otherwise - True
    """
    if  not os.path.isfile(archive_path):
        return False

    filename = os.path.basename(archive_path)
    name = os.path.splittext(filename)[0]

    if put(archive_path, "/tmp/{}".format(filename)).failed:
        return False

    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(filename, name)).failed:
        return False

    if run("rm /tmp/{}".format(filename)).failed:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name)).failed:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed:
        return False

    if run("rm -rf /data/web_static/current").failed:
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed:
        return False

    return True
