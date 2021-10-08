#!/usr/bin/env python3
# coding: utf8
import os,sys,pathlib,inspect
sys.path.append(str(pathlib.Path(__file__, '../../src').resolve()))
from FileReader import FileReader
from path import Path
import unittest
class TestFileReader(unittest.TestCase):
    def test_text(self):
        expected = """{
    "username": "はてなID",
    "api_key": "はてな AtomPub APIキー http://blog.hatena.ne.jp/my/config/detail"
}"""
        self.assertEqual(expected, FileReader.text(os.path.join(Path.parent(__file__, 2), 'src/secret-example.json')))
    def test_json(self):
        expected = {
            'username': 'はてなID',
            'api_key': 'はてな AtomPub APIキー http://blog.hatena.ne.jp/my/config/detail',
        }
        self.assertEqual(expected, FileReader.json(os.path.join(Path.parent(__file__, 2), 'src/secret-example.json')))

if __name__ == "__main__":
    unittest.main()
