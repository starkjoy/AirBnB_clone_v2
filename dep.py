#!/usr/bin/python3
"""Fabfile to create and distribute an archive to a web server"""

from fabric import task, Connection
import os.path

env = {"hosts": ["52.207.78.146", "35.175.64.54"]}

archive_path = "./versions"

@task
def do_deploy(c, archive_path):
    """Distributes an archive to a web server

    Args:
        c (fabric.Connection): The path of archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False
        Otherwise - True
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if c.put(archive_path, "/tmp/{}".format(file)).failed:
        return False

    if c.run("mkdir -p /data/web_static/releases/{}/".format(name)).failed:
        return False

    if c.run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name)).failed:
        return False

    if c.run("rm /tmp/{}".format(file)).failed:
        return False

    if c.run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name)).failed:
        return False

    if c.run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed:
        return False

    if c.run("rm -rf /data/web_static/current").failed:
        return False

    if c.run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed:
        return False

    return True
