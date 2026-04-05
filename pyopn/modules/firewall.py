from ..client import OPNClient

class Firewall:
    def __init__(self, client: OPNClient):
        self._client = client

        # Cache the different diagnostics modules
        self._filter = None
        self._alias_util = None
        self._alias = None
        self._filter_base = None

    @property
    def name(self):
        return self.__class__.__name__.lower()

    @property
    def filter(self):
        if self._filter is None:
            from ..controllers import Filter
            self._filter = Filter(self)

        return self._filter

    @property
    def filter_base(self):
        if self._filter_base is None:
            from ..controllers import FilterBase
            self._filter_base = FilterBase(self)

        return self._filter_base

    @property
    def alias_util(self):
        if self._alias_util is None:
            from ..controllers import AliasUtil
            self._alias_util = AliasUtil(self)

        return self._alias_util

    @property
    def alias(self):
        if self._alias is None:
            from ..controllers import Alias
            self._alias = Alias(self)

        return self._alias
