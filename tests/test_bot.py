def test_create():
    from pinbot.core.bot import create

    bot = create()
    assert bot
