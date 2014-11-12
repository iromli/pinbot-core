pinbot-core
===========

Write your bot:

.. sourcecode:: python

    # bot.py
    import pinbot.core.bot

    bot = pinbot.core.bot.create()
    bot.run()

Configure your bot:

.. sourcecode:: ini

    # config.ini
    [bot]
    host = irc.freenode.net
    port = 6667
    autojoins =
        pinbot

Run your bot:

.. sourcecode:: sh

    python bot.py config.ini
