#!/usr/bin/env python
try:
    import Cocoa  # python2.7 only
except ImportError:
    pass
import os
import public
import runcmd

import sys

APPLESCRIPT = """
use framework "Foundation"
use framework "AppKit"
use scripting additions

on run argv
    set _path to (item 1 of argv)
    set _image to (item 2 of argv)
    set theImage to (current application's NSImage's alloc()'s initWithContentsOfFile:_image)
    (current application's NSWorkspace's sharedWorkspace()'s setIcon:theImage forFile:_path options:0)
    return
end run
"""


def _cocoa_seticon(path, image):
    item = Cocoa.NSImage.alloc().initWithContentsOfFile_(path)
    Cocoa.NSWorkspace.sharedWorkspace().setIcon_forFile_options_(item, image, 0)


def _rm_dir_icon(path):
    icon = "%s/Icon\r" % path
    if os.path.exists(icon):
        os.unlink(icon)
        os.utime(path, None)  # touch (refresh Dock icon)


def _rm_file_icon(path):
    args = ["xattr", "-d", "com.apple.ResourceFork", path]
    runcmd.run(args)


@public.add
def rm(path):
    """remove icon"""
    fullpath = os.path.abspath(os.path.expanduser(path))
    if os.path.isdir(fullpath):
        _rm_dir_icon(fullpath)
    if os.path.isfile(fullpath):
        _rm_file_icon(fullpath)


@public.add
def update(path, image):
    """update icon"""
    if sys.version_info[0] == 2:
        return _cocoa_seticon(path, image)
    args = ["osascript", "-e", APPLESCRIPT, path, image]
    runcmd.run(args)._raise()
