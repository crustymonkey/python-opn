#import weakref
from typing import Any
from ..utils import LeafMixin


class Interface(LeafMixin):
    def __init__(self, parent: Any):
        #self._parent = weakref.proxy(parent)
        self._parent = parent

    @property
    def name(self) -> str:
        return self.__class__.__name__.lower()

    def get_interface_statistics(self) -> dict:
        """
        Retrieve interface statistics from the parent diagnostics module.
        
        Returns:
            dict: A dictionary containing interface statistics.
        """
        path = f'{self.get_path()}/get_interface_statistics'

        return self._parent._client._get_response(path).json()