#!/usr/bin/python3
from fabric.api import *
import os.path


env.hosts = ["52.3.250.108", "100.25.14.73"]


def do_deploy(archive_path):
    """A script that distributes an archive to web servers"""
    if not os.path.isfile(archive_path):
        return False
    file_path = os.path.basename(archive_path)
    name = os.path.splitext(file_path)[0]
    try:
        put(archive_path, "/tmp/{}".format(file_path))
        run("mkdir -p /data/web_static/releases/{}".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(file_path, name))
        run("rm /tmp/{}".format(file_path))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        return True
    except Exception:
        return False
