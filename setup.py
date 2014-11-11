from setuptools import setup

from pinbot.core import __version__


setup(
    name="pinbot-core",
    version=__version__,
    url="https://github.com/iromli/pinbot-core",
    author="Isman Firmansyah",
    license="MIT",
    zip_safe=False,
    install_requires=[
        "irc3",
        "six",
    ],
    packages=[
        "pinbot",
        "pinbot.core",
    ],
    entry_points={
        "console_scripts": ["pinbot=pinbot.core.cli:main"],
    },
    include_package_data=True,
)
