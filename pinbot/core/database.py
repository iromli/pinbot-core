from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import dataset
import irc3


@irc3.plugin
class Dataset(object):
    def __init__(self, bot):
        self.bot = bot
        self._db = None

    @property
    def db(self):
        if self._db is None:
            self._db = dataset.connect(
                self.bot.config.get("database_url", "sqlite:///pinbot.db"))
        return self._db
