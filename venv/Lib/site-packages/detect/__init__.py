#!/usr/bin/env python
import sys

# os
_platform = sys.platform.lower()


freebsd = "freebsd" in _platform
linux = "linux" in _platform
mac = "darwin" in _platform
osx = "darwin" in _platform
windows = "win32" in _platform or "cygwin" in _platform
cygwin = "cygwin" in _platform
unix = not windows and not cygwin

# python versions


py2 = sys.version_info[0] == 2
py3 = sys.version_info[0] == 3
