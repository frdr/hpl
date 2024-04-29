#!/usr/bin/env python3
# vim: fileencoding=utf-8
"""
The Hello World Programming Language Core Module
"""
__author__ = 'Friedrich C. Kischkel <friedrich.kischkel@gmail.com>'
__copyright__ = 'Copyright (C) 2023 Friedrich C. Kischkel. All rights reserved.'
__license__ = 'Public domain'

_keywords = {
    'hello world!': 'print("hello world!")',
    'Hello World!': 'print("Hello World!")',
}


def hpl_eval(arg):
    """Evaluate arg - this is where the magic happens!"""
    if not arg:
        print("hello world!")
    else:
        # Run "legacy" script
        eval(arg)


def parse(arg):
    for word in _keywords:
        if word in arg:
            pass
