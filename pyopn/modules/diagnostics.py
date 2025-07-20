#import weakref
from ..client import OPNClient

class Diagnostics:
    def __init__(self, client: OPNClient):
        #self._client = weakref.proxy(client)
        self._client = client

    @property
    def name(self):
        return self.__class__.__name__.lower()

    @property
    def interface(self):
        from .interface import Interface

        return Interface(self)