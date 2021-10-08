#!/usr/bin/env python3
# coding: utf8
import os,sys,pathlib,inspect
sys.path.append(str(pathlib.Path(__file__, '../../src').resolve()))
from wsse import WSSE
import unittest
from path import Path
from FileReader import FileReader
class TestWSSE(unittest.TestCase):
    def test_from_str(self):
        username = 'user1'
        api_key = 'key1'
        headers = WSSE.from_str(username, api_key)
        self.assertTrue('X-WSSE' in headers)
        self.assertTrue(username in headers['X-WSSE'])
        self.assertTrue('UsernameToken ' in headers['X-WSSE'])
        self.assertTrue('Username=' in headers['X-WSSE'])
        self.assertTrue('PasswordDigest=' in headers['X-WSSE'])
        self.assertTrue('Nonce=' in headers['X-WSSE'])
        self.assertTrue('Created=' in headers['X-WSSE'])
    def test_from_json(self):
        path = os.path.join(Path.parent(__file__, 2), 'src/secret-example.json')
        username = FileReader.json(path)['username']
        api_key = FileReader.json(path)['api_key']
        headers = WSSE.from_json(path)
        self.assertTrue('X-WSSE' in headers)
        self.assertTrue(username in headers['X-WSSE'])
        self.assertTrue('UsernameToken ' in headers['X-WSSE'])
        self.assertTrue('Username=' in headers['X-WSSE'])
        self.assertTrue('PasswordDigest=' in headers['X-WSSE'])
        self.assertTrue('Nonce=' in headers['X-WSSE'])
        self.assertTrue('Created=' in headers['X-WSSE'])
    def test_from_json_with_schema(self):
        path = os.path.join(Path.parent(__file__, 2), 'src/secret-example.json')
        path_schema = os.path.join(Path.parent(__file__, 2), 'src/secret-schema.json')
        username = FileReader.json(path)['username']
        api_key = FileReader.json(path)['api_key']
        headers = WSSE.from_json(path, path_schema)
        self.assertTrue('X-WSSE' in headers)
        self.assertTrue(username in headers['X-WSSE'])
        self.assertTrue('UsernameToken ' in headers['X-WSSE'])
        self.assertTrue('Username=' in headers['X-WSSE'])
        self.assertTrue('PasswordDigest=' in headers['X-WSSE'])
        self.assertTrue('Nonce=' in headers['X-WSSE'])
        self.assertTrue('Created=' in headers['X-WSSE'])

if __name__ == "__main__":
    unittest.main()
