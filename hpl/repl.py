#!/usr/bin/env python3
# vim: fileencoding=utf-8
"""
"""
__author__ = 'Friedrich C. Kischkel <friedrich.kischkel@gmail.com>'
__copyright__ = 'Copyright (C) 2023 Friedrich C. Kischkel. All rights reserved.'
__license__ = 'Public domain'

import traceback
import core


def prompt():
    """A prompt to use in interactive sessions"""
    return "hello? "


def repl():
    """Show a REPL for interactive use."""
    eval = core.hpl_eval
    while True:
        try:
            result = eval(input(prompt()))
            if result:
                print(result)
        except Exception as err:
            # HPL script can _never_ throw exceptions but legacy script can
            traceback.print_exception(err)


if __name__ == '__main__':
    repl()
