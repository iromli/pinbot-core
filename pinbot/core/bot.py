from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import irc3

from . import config


def create():
    settings = {
        "nick": "__pinbot__",
        "realname": "pinbot",
        "host": "irc.freenode.net",
        "port": 6667,
    }
    settings.update(config.resolve())
    bot = irc3.IrcBot(**settings)
    return bot
