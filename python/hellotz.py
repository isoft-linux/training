#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import time
try:
    import leslie_tz
except ImportError:
    if sys.version_info.major != 3:
        print("--------Please Install Leslie TimeZone Python Binding--------")
        print("```sudo python2 setup.py install```")
        print("-------------------------------------------------------------")

if sys.version_info.major == 3:
    print(int(time.localtime().tm_gmtoff / 3600))
else:
    print(leslie_tz.gmtoff())
