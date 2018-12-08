#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import public
import mkdir


def _convert_bytes(content):
    """
    TypeError: str() takes at most 1 argument (2 given) # python2
    """
    try:
        return str(content, "utf-8")
    except TypeError:
        return str(content)


def _convert(content):
    if content is None:
        return ""
    if str(content.__class__) == "<class 'bytes'>":
        return _convert_bytes(content)
    return str(content)


@public.add
def write(path, content):
    """write content to file. Creates directory if it doesn't exist"""
    fullpath = os.path.abspath(os.path.expanduser(path))
    content = _convert(content)
    mkdir.mkdir(os.path.dirname(fullpath))
    try:
        unicode()
        if isinstance(content, unicode):
            content = content.encode("utf-8")
        open(fullpath, "w").write(content)
    except NameError:
        """NameError: name 'unicode' is not defined"""
        open(fullpath, "w", encoding="utf-8").write(content)
    return fullpath
