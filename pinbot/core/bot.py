from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import irc3

from . import config


def create():
    settings = config.resolve()
    bot = irc3.IrcBot(**settings)
    return bot
