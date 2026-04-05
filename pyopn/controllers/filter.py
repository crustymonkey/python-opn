from typing import Any
from ..utils import LeafMixin


class Filter(LeafMixin):
    def __init__(self, parent: Any):
        self._parent = parent
        # These are all the GET methods that can be called without params
        self._methods = (
            'get_interface_list',
        )

    @property
    def name(self) -> str:
        return self.__class__.__name__.lower()

    def __getattr__(self, name):
        """
        This will dynamically build the path and return the results of
        one of the GET API calls in this controller
        """
        if name not in self._methods:
            raise NotImplementedError(
                f'method with name "{name}" does not exist')

        path = f'{self.get_path()}/{name}'

        return lambda: self._parent._client._get_response(path).json()

    def search_rule(self):
        path = f'{self.get_path()}/search_rule'

        return lambda: self._parent._client._get_response(path).json()
