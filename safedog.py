#!/usr/bin/env python

"""
Copyright (c) 2006-2020 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.core.data import kb
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):

    retVal = payload

    if payload:
        retVal = retVal.replace('UNION', '/*!50445union*/')
        retVal = retVal.replace('SELECT', '/*!50445select*/')
        retVal = retVal.replace('USER()', 'usEr/*!(*/)')
        retVal = retVal.replace(' ', '/**/')
        retVal = retVal.replace('OR', '/*!50445OR*/')
        retVal = retVal.replace('AND', '/*!50445AND*//')

    return retVal