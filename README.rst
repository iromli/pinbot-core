pinbot-core
===========

.. image:: https://codeship.com/projects/9d59e1a0-6a81-0132-7e67-2e196b4816c1/status?branch=master
    :alt: Codeship status

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
