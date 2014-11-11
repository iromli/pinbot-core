pinbot-core
===========

Simple usage::

    PINBOT_HOST='irc.freenode.net' PINBOT_PORT=6667 PINBOT_AUTOJOINS='#pinbot' PINBOT_NICK='__pinbot__' \
        python -c 'import pinbot.core.bot; pinbot.core.bot.create().run()'
