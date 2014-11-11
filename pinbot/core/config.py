from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import os
from itertools import takewhile

import six


def _from_file(path):
    settings = {}

    with open(path) as f:
        exec(f.read(), {}, settings)

    return {
        k: v for k, v in six.iteritems(settings)
        if k.isupper() and k.startswith("PINBOT_")
    }


def _from_environ():
    return {
        k: v for k, v in six.iteritems(os.environ)
        if k.startswith("PINBOT_")
    }


def _resolve_comma_values(values):
    resolved = takewhile(
        lambda v: v,
        [item.strip() for item in values.split(",")],
        )
    return list(resolved)


def resolve():
    settings = {}
    conf = os.environ.get("PINBOT_CONFIG")

    if conf:
        settings.update(_from_file(conf))

    settings.update(_from_environ())

    settings = {
        k.lower().replace("pinbot_", ""): v for k, v in six.iteritems(settings)
    }

    for csv in ("autojoins", "includes"):
        if csv in settings:
            settings[csv] = _resolve_comma_values(settings[csv])
    return settings
