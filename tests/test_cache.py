import unittest

from task2.cache import Cache


class TestCache(unittest.TestCase):
    def setUp(self):
        self.cache = Cache()

    def test_set_key(self):
        self.cache.set_key('somekey', 'somevalue')
        self.assertIn('somekey', self.cache._data)

    def test_get_key_value(self):
        self.cache.set_key('somekey', 'somevalue')
        self.assertEqual(self.cache.get_key_value('somekey'), 'somevalue')

    def test_make_key(self):
        self.assertEqual(self.cache.make_key('fn', 'arg1', 'arg2',
                                             kwarg='value'),
                         '["fn", "arg1", "arg2"]:{"kwarg": "value"}')
