#!/usr/bin/env python3
# coding: utf8
from base64 import b64encode
from datetime import datetime
from hashlib import sha1
import random
import json
import jsonschema 
from FileReader import FileReader
class WSSE:
    @classmethod
    def from_str(cls, username:str, api_key:str):
        return cls._make_header(username, api_key)
    @classmethod
    def from_json(cls, path, schema_path=None):
        secret = FileReader.json(path)
        if schema_path:
            schema = FileReader.json(schema_path)
            try:
                jsonschema.validate(secret, schema)
            except jsonschema.ValidationError as e:
                print('[ERROR] secret.json 形式エラーです。secret-schema.json に従ってください。', file=sys.stderr)
                print(e, file=sys.stderr)
                raise e
        return cls._make_header(secret['username'], secret['api_key'])
    @classmethod
    def _make_header(cls, username:str, api_key:str):
        return {'X-WSSE': cls._wsse(username, api_key)}
    @classmethod
    def _wsse(cls, username:str, api_key:str) -> str:
        created = datetime.now().isoformat() + "Z"
        b_nonce = sha1(str(random.random()).encode()).digest()
        b_digest = sha1(b_nonce + created.encode() + api_key.encode()).digest()
        return f'UsernameToken Username="{username}", PasswordDigest="{b64encode(b_digest).decode()}", Nonce="{b64encode(b_nonce).decode()}", Created="{created}"'
