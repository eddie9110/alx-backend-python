#!/usr/bin/env python3
""" 
Script contains tests for class uclient.GithubOrgClient
"""

import unittest
from unittest.mock import PropertyMock, patch, Mock
from unittest import mock
from client import GithubOrgClient
from parameterized import parameterized
import requests
import json


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests for GithobOrgClient
    """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """ method tests that GithubOrgClient.org
        returns the correct value."""
        result_= GithubOrgClient(input)
        result_.org()
        mock.called_with_once(result_.ORG_URL)

    def test_has_license(self, repo, key, expectation):
        """testing if repo has a license"""
        self.assertEqual(GithubOrgClient.has_license(repo, key), expectation)

if __name__ == '__main__':
    unittest.main()
