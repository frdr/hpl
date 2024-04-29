#!/usr/bin/env python3
# vim: fileencoding=utf-8
"""
"""
__author__ = 'Friedrich C. Kischkel <friedrich.kischkel@gmail.com>'
__copyright__ = 'Copyright (C) 2023 Friedrich C. Kischkel. All rights reserved.'
__license__ = 'Public domain'

import sys
import fileinput
from . import core
from . import repl

if len(sys.argv) == 1:
    sys.exit(repl.repl())
else:
    for line in sys.argv[1:]:
        core.hpl_eval(line)
    sys.exit()
