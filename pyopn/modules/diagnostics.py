from ..client import OPNClient

class Diagnostics:
    def __init__(self, client: OPNClient):
        self._client = client

        # Cache the different diagnostics modules
        self._interface = None

    @property
    def name(self):
        return self.__class__.__name__.lower()

    @property
    def interface(self):
        if self._interface is None:
            from .interface import Interface
            self._interface = Interface(self)


        return self._interface
