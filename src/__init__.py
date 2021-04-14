import gevent.monkey

from src.version import __version__

gevent.monkey.patch_all()