#!/usr/bin/env python
"""read/write webloc url"""
import click
import os
import plistlib
import public


@public.add
def read(path):
    """return webloc url"""
    plist = plistlib.readPlist(path)
    return plist.URL


@public.add
def write(path, url):
    """write url to webloc file"""
    rootObject = dict(URL=str(url))
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
    plistlib.writePlist(rootObject, path)


@click.command()
@click.argument('path')
@click.argument('url', required=False)
def _cli(path, url=None):
    if not url:
        url = read(path)
        if url:
            print(url)
    else:
        write(path, url)


MODULE_NAME = "webloc"
USAGE = 'python -m %s [url]' % MODULE_NAME
PROG_NAME = 'python -m %s' % MODULE_NAME


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
