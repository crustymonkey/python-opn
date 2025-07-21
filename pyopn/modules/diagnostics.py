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
        from .interface import Interface
        if self._interface is None:
            self._interface = Interface(self._client)

        return self._interface