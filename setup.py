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
        "dataset",
        "configparser",
        "docopt",
    ],
    packages=[
        "pinbot",
        "pinbot.core",
    ],
    include_package_data=True,
)
