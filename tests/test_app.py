from unittest.mock import patch
import unittest

from task2.app import Task2


class TestTask2(unittest.TestCase):
    def setUp(self):
        self.app = Task2()

    def test_get_fibonacci(self):
        self.assertEqual(self.app.get_fibonacci(4), [0, 1, 1, 2])

    def test_get_fibonacci_piece(self):
        self.assertEqual(self.app._get_fibonacci_piece(4), 3)

    @patch('task2.cache.Cache.get_key_value', return_value=0)
    def test_get_fibonacci_piece_cache(self, mock_cache_get_key_value):
        # Check if a cache key/value is created.
        self.assertEqual(self.app._get_fibonacci_piece(0), 0)

        # Call it a second time, check if cache is called instead of executed
        self.assertEqual(self.app._get_fibonacci_piece(0), 0)

        mock_cache_get_key_value.assert_called_once()

    def test_get_app_status(self):
        self.assertEqual(self.app.get_app_status(),
                         {'app_calls': 0, 'cached_keys': 0, 'expired_keys': 0})

        # Increase app calls and cached keys
        self.app.get_fibonacci(4)
        self.assertEqual(self.app.get_app_status(),
                         {'app_calls': 1, 'cached_keys': 4, 'expired_keys': 0})
