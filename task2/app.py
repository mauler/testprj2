import logging

from task2.cache import Cache


LOGGER = logging.getLogger(__name__)


def cache(fn):
    """Makes function calls cacheable."""

    def decorated(app, *args, **kwargs):
        cachekey = app._cache.make_key(fn.__name__, *args, **kwargs)
        timeout = app._cache.get_key_info(cachekey)
        if timeout is None:
            value = fn(app, *args, **kwargs)
            LOGGER.debug('Setting cache value: {}'.format(cachekey))
            app._cache.set_key(cachekey, value)
            return value
        else:
            LOGGER.debug('Retrieving cache value: {}'.format(cachekey))
            return app._cache.get_key_value(cachekey)

    return decorated


class Task2:
    def __init__(self):
        self._cache = Cache()
        self._calls = 0

    @cache
    def _get_fibonacci_piece(self, number):
        """Returns the fibonacci piece of a number.

        :param number:  the number
        :type number: int
        :returns: The fibonacci piece
        :rtype: int
        """
        a, b = 0, 1
        while number > 0:
            a, b = b, a + b
            number -= 1
        return a

    def _compute_call(self):
        """Computes an app call."""
        self._calls += 1

    def get_fibonacci(self, number, start=0):
        """Returns the fibonacci sequence for the desired number.

        :param number:  the desired number
        :type number: int

        :param start:  the start of the sequence
        :type start: int

        :returns: The fibonacci sequence
        :rtype: List[int]
        """
        self._compute_call()
        LOGGER.info('Generating fibonacci for range: {}, {}'.format(start,
                                                                    number))
        return [self._get_fibonacci_piece(n) for n in range(start, number)]

    def get_app_status(self):
        """Returns general app running status. """
        cached_keys = 0
        expired_keys = 0
        for key, value in self._cache._data.items():
            cached_keys += 1
            timeout = self._cache.get_key_info(key)
            if timeout is None:
                expired_keys += 1

        return {
            'app_calls': self._calls,
            'cached_keys': cached_keys,
            'expired_keys': expired_keys,
        }
