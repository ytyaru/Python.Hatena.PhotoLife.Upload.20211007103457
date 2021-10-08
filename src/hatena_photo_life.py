#!/usr/bin/env python3
# coding: utf8
import os
from base64 import b64encode
import requests
import mimetypes
import xmltodict
import pathlib
from path import Path
class HatenaPhotoLife:
    def __init__(self, headers:dict=None):
        self.__headers = headers if headers else {}
        self.__base_url = 'https://f.hatena.ne.jp/atom'
    def post(self, path:str, title:str=None, folder:str=None, generator:str=None):
        if not os.path.isfile(path): raise FileNotFoundError(f'[ERROR] 指定されたファイルは存在しません。: {path}\nhttps://f.hatena.ne.jp/help')
        mimetype = mimetypes.guess_type(path)[0]
        if Path.ext(path).lower() not in ['.png', '.jpg', '.jpeg', '.gif']: raise ValueError(f'[ERROR] 指定されたファイルはpng,jpg,gifのいずれでもありません。: {path}\nhttps://f.hatena.ne.jp/help')
        if 10*1000*1000 < os.path.getsize(path): raise ValueError(f'[ERROR] 指定されたファイルのサイズは10MBを超えています。: {path}\nhttps://f.hatena.ne.jp/help')

        data = self._make_request_data(
            path = path,
            title = os.path.basename(path) if not title else title,
            folder = folder,
            generator = generator)
        return requests.post(self.PostUri, data=data, headers=self.__headers)
    def set_title(self, image_id:str, title:str):
        return requests.put(f'{self.EditUri}/{image_id}', data=self._make_request_data(title=title), headers=self.__headers)
    def delete(self, image_id:str):
        return requests.delete(f'{self.EditUri}/{image_id}', headers=self.__headers)
    def get(self, image_id:str):
        return requests.get(f'{self.EditUri}/{image_id}', headers=self.__headers)
    def feed(self):
        return requests.get(self.FeedUri, headers=self.__headers)
    def _make_request_data(self, path:str=None, title:str=None, folder:str=None, generator:str=None) -> str:
        if path and not title: title = os.path.basename(path)
        title = '' if not title else f'<title>{title}</title>'
        content = '' if not path else f'<content mode="base64" type="{mimetypes.guess_type(path)[0]}">{b64encode(pathlib.Path(path).read_bytes()).decode()}</content>'
        folder = '' if not folder else f'<dc:subject>{folder}</dc:subjetct>'
        generator = '' if not generator else f'<generator>{generator}</generator>'
        return f'<entry xmlns="http://purl.org/atom/ns#">{title}{content}{folder}{generator}</entry>'
    @property
    def PostUri(self): return f'{self.__base_url}/post'
    @property
    def EditUri(self): return f'{self.__base_url}/edit'
    @property
    def FeedUri(self): return f'{self.__base_url}/feed'

