#!/usr/bin/env python
"""set icon"""
import os
import click
import mac_icon

MODULE_NAME = "mac_icon.set"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = "python -m %s path image" % MODULE_NAME


def _fullpath(path):
    return os.path.abspath(os.path.expanduser(path))


@click.command()
@click.argument('path', required=True)
@click.argument('image', required=True)
def _cli(path, image):
    mac_icon.update(path, image)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
