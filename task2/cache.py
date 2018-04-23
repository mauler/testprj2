from datetime import datetime, timedelta
from json import dumps


class Cache:
    """Helper class to abstract caching based on key -> value. """

    def __init__(self):
        self._data = {}
        self._data_timeout = {}

    def get_key_value(self, key):
        """Returns cache key value.

        :param key: the key
        :type key: str

        :returns: anything
        :rtype: any
        """
        return self._data[key]

    def get_key_info(self, key):
        """Returns keys expiration time in seconds or None if already expired.

        :param key: the key
        :type key: str

        :returns: timeout in seconds
        :rtype: int or None
        """
        if key not in self._data:
            return None
        else:
            return (self._data_timeout[key] - datetime.now()).seconds

    def make_key(self, *args, **kwargs):
        """Make a serialized key based on a function call.

        :param args: tuple with function call args
        :type args: tuple

        :param kwargs: dict with function call args
        :type kwargs: dict

        :returns: key serialized string
        :rtype: str
        """
        return '{}:{}'.format(dumps(args), dumps(kwargs, sort_keys=True))

    def set_key(self, key, value, timeout=30):
        """Sets key value.

        :param key: cache key
        :type key: str

        :param value: the value to be saved.
        :type value: any

        :returns: expiration datetime
        :rtype: datetime.datetime
        """
        self._data[key] = value
        self._data_timeout[key] = datetime.now() + timedelta(seconds=timeout)
        return self._data_timeout[key]
