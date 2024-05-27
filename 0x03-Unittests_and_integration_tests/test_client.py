#!/usr/bin/env python3
"""
Test module for client.GithubOrgClient class
"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import utils


class TestGithubOrgClient(unittest.TestCase):
    """test for GithubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        """ Tests the return value"""

        org_test = GithubOrgClient(org)
        test_response = org_test.org
        self.assertEqual(test_response, mock_org.return_value)
        mock_org.assert_called_once()

    def test_public_repos_url(self):
        """ Tests the result of _public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "Hello World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
        },
    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration tests"""

    @classmethod
    def setUpClass(cls):
        """ setup method"""

        route_payload = {
                'https://api.github.com/orgs/google': cls.org_payload,
                'https://api.github.com/orgs/google/repos': cls.repos_payload,
                }

        def get_payload(url):
            """ returns mock payload"""
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError
        cls.get_patcher = patch('utils.requests.get', side_effect=get_payload)
        cls.get_patcher.start()
        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        """ Called at the end of test"""

        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Tests the public repos"""

        self.assertEqual(self.client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """ Tests public repos with license"""

        self.assertEqual(
                GithubOrgClient("google").public_repos(license="apache-2.0"),
                self.apache2_repos,
                )
