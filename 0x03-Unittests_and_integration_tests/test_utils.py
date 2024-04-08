#!/usr/bin/env python3
"""
Script to unit test for utils.access_nested_map
"""

import unittest
from unittest import mock
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
import requests
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """access_nested_map tests"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, dict, path, expected):
        """test access nested map."""
        self.assertEqual(access_nested_map(dict, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, dict, path):
        """test_access_nested_map_exception"""
        with self.assertRaises(KeyError):
            access_nested_map(dict, path)


class TestGetJson(unittest.TestCase):
    """class containing tests for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """method to test that utils.get_json
        returns the expected result."""
        class Mocked(Mock):
            """Mocked Class"""

            def json(self):
                """method returns test_payload"""
                return test_payload

        with patch('requests.get') as m:
            m.return_value = Mocked()
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test Mmemoize
    """
    def test_memoize(self):
        """tests to mock a_method"""

        class TestClass:
            """
            Test Class
            """
            def a_method(self):
                """a_method"""
                return 42

            @memoize
            def a_property(self):
                """a_property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            x = TestClass()
            x.a_property
            x.a_property
            mock_method.assert_called_once()
