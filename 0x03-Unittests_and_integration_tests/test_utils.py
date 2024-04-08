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
