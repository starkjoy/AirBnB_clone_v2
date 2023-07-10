#!/usr/bin/python3
"""Fabfile to create and distribute an archive to a web server"""

from fabric import Connection, Config, task
import os

key = "./key.rsa"

server_ips = ["52.207.78.146", "35.175.64.54"]

archive_path = "./versions"

@task
def do_deploy(c):
    """Distributes an archive to a web server

    Args:
        c (fabric.Connection): The path of archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False
        Otherwise - True
    """
    file_paths = [os.path.join(archive_path, f) for f in os.listdir(archive_path) if f.endswith(".tgz")]

    for file_path in file_paths:

        filename = os.path.basename(file_path)
        name = os.path.splitext(filename)[0]

        config = Config(overrides={'sudo': {'password': ''}})

        for server_ip in server_ips:
            conn = Connection(host=server_ip, user='ubuntu', connect_kwargs={'key_filename': key}, config=config)

            with conn.cd('/'):

                if conn.put(file_path, "/tmp/{}".format(filename)).failed:
                    return False

                if conn.run("mkdir -p /data/web_static/releases/{}/".format(name)).failed:
                    return False

                if conn.run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(filename, name)).failed:
                    return False

                if conn.run("rm /tmp/{}".format(filename)).failed:
                    return False

                if conn.run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name)).failed:
                    return False

                if conn.run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed:
                    return False

                if conn.run("rm -rf /data/web_static/current").failed:
                    return False

                if conn.run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed:
                    return False

    return True
