from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import os

import pytest
import six


def test_from_file(tmpdir):
    from pinbot.core.config import _from_file

    file_ = tmpdir.mkdir("pinbot_core").join("config.py")
    file_.write('PINBOT_HOST = "example.com"')

    settings = _from_file(six.text_type(file_))
    assert "PINBOT_HOST" in settings


def test_from_environ():
    from pinbot.core.config import _from_environ

    os.environ["PINBOT_HOST"] = "example.com"
    settings = _from_environ()
    assert "PINBOT_HOST" in settings


@pytest.mark.parametrize("values, size", [
    ("#chan1,#chan2", 2),
    ("#chan1, #chan2,", 2),
    (" #chan1 , #chan2 ,", 2),
    (" #chan1 , #chan2 , ", 2),
])
def test_resolve_comma_values(values, size):
    from pinbot.core.config import _resolve_comma_values

    resolved = _resolve_comma_values(values)
    assert len(resolved) == size


def test_resolve(tmpdir):
    from pinbot.core.config import resolve

    file_ = tmpdir.mkdir("pinbot_core").join("config.py")
    file_.write('PINBOT_HOST = "example.com"')

    os.environ["PINBOT_CONFIG"] = six.text_type(file_)

    settings = resolve()
    assert "host" in settings


def test_resolve_with_autojoins(tmpdir):
    from pinbot.core.config import resolve

    file_ = tmpdir.mkdir("pinbot_core").join("config.py")
    file_.write('PINBOT_AUTOJOINS = "#foo, #bar"')

    os.environ["PINBOT_CONFIG"] = six.text_type(file_)
    settings = resolve()
    assert settings["autojoins"] == ["#foo", "#bar"]


def test_resolve_masks():
    from pinbot.core.config import _resolve_masks

    settings = _resolve_masks({
        "masks_random": "johndoe!*@*,janedoe!*@*",
    })
    actual = {"johndoe!*@*": "random", "janedoe!*@*": "random"}
    assert settings["irc3.plugins.command.masks"] == actual
