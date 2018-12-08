#!/usr/bin/env python
import public
import requests

TIMEOUT = 5
URL = 'http://www.google.com/'


@public.add
def check(timeout=None):
    """return True if connection is ok, else False"""
    if not timeout:
        timeout = TIMEOUT
    try:
        requests.get(URL, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False
    return False
