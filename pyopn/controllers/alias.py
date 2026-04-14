from typing import Any, List
from ..utils import LeafMixin


class Alias(LeafMixin):
    def __init__(self, parent: Any):
        self._parent = parent
        # These are all the GET methods that can be called without params
        self._methods = (
            'get',
            'list_network_aliases',
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

    def search_item(self, search: str=None):
        params = {
            'current': 1,
            'rowCount': 50,
            'sort': {},
        }

        if search:
            params['searchPhrase'] = search

        path = f'{self.get_path()}/search_item'

        return self._parent._client._get_response(path, params, 'POST').json()

    def set_item(self, uuid: str, content: List[str]):
        params = {'alias': {
            'content': '\n'.join([s.strip() for s in content]),
            'enabled': '1',
        }}

        path = f'{self.get_path()}/set_item/{uuid}'

        return self._parent._client._get_response(path, params, 'POST').json()

    def get_item(self, uuid: str):
        path = f'{self.get_path()}/get_item/{uuid}'

        return self._parent._client._get_response(path).json()

    def get_alias_uuid(self, name: str):
        path = f'{self.get_path()}/get_alias_u_u_i_d/{name}'

        return self._parent._client._get_response(path).json()

    def get_alias_u_u_i_d(self, name: str):
        return self.get_alias_uuid(name)

    def get_geo_ip(self):
        return self.get_geo_i_p()
