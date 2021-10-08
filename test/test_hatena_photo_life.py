#!/usr/bin/env python3
# coding: utf8
import os,sys,pathlib,inspect
sys.path.append(str(pathlib.Path(__file__, '../../src').resolve()))
from wsse import WSSE
import unittest
from unittest import mock
import requests
from path import Path
from FileReader import FileReader
from hatena_photo_life import HatenaPhotoLife
class TestHatenaPhotoLife(unittest.TestCase):
    @mock.patch("requests.post")
    def test_post_not_exist_file(self, mock_post):
        username = 'user1'
        api_key = 'key1'
        headers = WSSE.from_str(username, api_key)
        api = HatenaPhotoLife(headers)
        with self.assertRaises(FileNotFoundError, msg='指定されたファイルは存在しません'):
            api.post('')
    @mock.patch("requests.post")
    def test_post_not_support_type(self, mock_post):
        username = 'user1'
        api_key = 'key1'
        headers = WSSE.from_str(username, api_key)
        api = HatenaPhotoLife(headers)
        with self.assertRaises(ValueError, msg='指定されたファイルはpng,jpg,gifのいずれでもありません'):
            api.post(Path.here('test_data/test.svg'))
    @mock.patch("requests.post")
    def test_post_over_size(self, mock_post):
        username = 'user1'
        api_key = 'key1'
        headers = WSSE.from_str(username, api_key)
        api = HatenaPhotoLife(headers)
        with self.assertRaises(ValueError, msg='指定されたファイルのサイズは10MBを超えています'):
            api.post(Path.here('test_data/over_size.png'))
    @mock.patch("requests.post")
    def test_post_support_types(self, mock_post):
        username = 'user1'
        api_key = 'key1'
        headers = WSSE.from_str(username, api_key)
        api = HatenaPhotoLife(headers)
        api.post(Path.here('test_data/test.png'))
        api.post(Path.here('test_data/test.jpg'))
        api.post(Path.here('test_data/test.gif'))
    @mock.patch("requests.put")
    def test_set_title(self, mock_post):
        username = 'user1'
        api_key = 'key1'
        headers = WSSE.from_str(username, api_key)
        api = HatenaPhotoLife(headers)
        api.set_title('yyyyMMddHHmmss', 'new-title')
    @mock.patch("requests.delete")
    def test_delete(self, mock_post):
        username = 'user1'
        api_key = 'key1'
        headers = WSSE.from_str(username, api_key)
        api = HatenaPhotoLife(headers)
        api.delete('yyyyMMddHHmmss')
    @mock.patch("requests.get")
    def test_get(self, mock_post):
        username = 'user1'
        api_key = 'key1'
        headers = WSSE.from_str(username, api_key)
        api = HatenaPhotoLife(headers)
        api.get('yyyyMMddHHmmss')
    @mock.patch("requests.get")
    def test_feed(self, mock_post):
        username = 'user1'
        api_key = 'key1'
        headers = WSSE.from_str(username, api_key)
        api = HatenaPhotoLife(headers)
        api.feed()


if __name__ == "__main__":
    unittest.main()
