from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import irc3

from . import config


def main():
    settings = config.resolve()
    bot = irc3.IrcBot(**settings)
    bot.run()
