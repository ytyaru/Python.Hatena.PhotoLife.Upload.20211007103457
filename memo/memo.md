# ヘルプ

```markdown
画像をアップロードする。はてなフォトライフへ。	${VERSION}
${THIS_NAME} [-t title] [-f folder] [-g generator] [-p response-parser] PATH
Auguments:
  PATH                  画像ファイルパス
Options:
  -t --title              画像のタイトル。初期値はPATHのファイル名。
  -f --folder             アップロード先のフォルダ名。
  -g --generator          アップロードしたツール名（フォルダ振分用）
  -p --response-parser    API応答をパースするメソッドを指定する。[default: ListupResponseParser.py]
                          デフォルトでは以下3つを1行おきに出力する。
                          hatena:imageurl, hatena:imageurlsmall, hatena:syntax
Settings:
  secret.json
    username:      はてなID
    api_key:       AtomPub API key http://blog.hatena.ne.jp/my/config/detail
    folder:        デフォルトのアップロード先フォルダ名
    folders:       アップロード先フォルダ名のリスト
    generator:     デフォルトのアップロードツール名
    generators:    アップロードツール名のリスト
    output_format: デフォルトの出力形式
API Documents:
  https://f.hatena.ne.jp/help
  http://developer.hatena.ne.jp/ja/documents/fotolife/apis/atom
  http://developer.hatena.ne.jp/ja/documents/auth/apis/wsse
output-exmaple:
  URL: https://cdn-ak.f.st-hatena.com/images/fotolife/y/ytyaru/20211006/20211006125842.png
  ID:  f:id:ytyaru:20211006125842p:image
```

# API Documents

* https://f.hatena.ne.jp/help
* http://developer.hatena.ne.jp/ja/documents/fotolife/apis/atom
* http://developer.hatena.ne.jp/ja/documents/auth/apis/wsse

# output-exmaple

* URL: https://cdn-ak.f.st-hatena.com/images/fotolife/y/ytyaru/20211006/20211006125842.png
* ID:  f:id:ytyaru:20211006125842p:image

# ワークフロー

* APIをリクエストする
  * HTTP Request
  * 認証
    * WEES認証
      * はてなID
      * APIKey
* レスポンスを受け取る




## はてなフォトライフAPIクライアント

### lib.py

```python
import inspect
class Path:
    @classmethod
    def current(cls, path): # カレントディレクトリからの絶対パス
        return cls.__expand(os.path.join(os.getcwd(), path))
    @classmethod
    def here(cls, path): # このファイルからの絶対パス（呼出元ファイルを基準としたパス）
        return cls.__expand(os.path.join(os.path.dirname(os.path.abspath(inspect.stack()[1].filename)), path))
#        return cls.__expand(os.path.join(os.path.dirname(os.path.abspath(__file__)), path))
    @classmethod
    def name(cls, path): # このファイル名
        return os.path.basename(path)
    @classmethod
    def this_name(cls): # このファイル名
        return os.path.basename(__file__)
    @classmethod
    def ext(cls, path=__file__): # このファイルの拡張子
        return os.path.splitext(os.path.basename(path))[1]
    @classmethod
    def __expand(cls, path): # homeを表すチルダや環境変数を展開する
        return os.path.expandvars(os.path.expanduser(path))
class FileReader:
    @classmethod
    def read(cls, path):
        if '.json' == Path.ext(path).lower(): return cls.json(path)
        else: return cls.text(path)
    @classmethod
    def text(cls, path):
        with open(path, mode='r', encoding='utf-8') as f: return f.read().rstrip('\n')
    @classmethod
    def json(cls, path):
        with open(path, mode='r', encoding='utf-8') as f: return json.load(f)
```
```python
```

wsse.py
```python
from base64 import b64encode
from datetime import datetime
from hashlib import sha1
import random
import json
import jsonschema 
class WSSE:
    @classmethod
    def from_str(cls, username:str, api_key:str):
        return cls._make_header(username, api_key)
    @classmethod
    def from_json(cls, path):
        schema = FileReader.json(Path.here('secret-schema.json'))
        secret = FileReader.json(Path.here('secret.json'))
        try:
            jsonschema.validate(secret, schema)
            return cls._make_header(username, api_key)
        except jsonschema.ValidationError as e:
            print('[ERROR] secret.json 形式エラーです。secret-schema.json に従ってください。', file=sys.stderr)
            print(e, file=sys.stderr)
            raise e
    @classmethod
    def _make_header(cls, username:str, api_key:str):
        return {'X-WSSE': self._wsse(username, api_key)}
    @classmethod
    def _wsse(cls, username:str, api_key:str) -> str:
        created = datetime.now().isoformat() + "Z"
        b_nonce = sha1(str(random.random()).encode()).digest()
        b_digest = sha1(b_nonce + created.encode() + api_key.encode()).digest()
        return f'UsernameToken Username="{username}", PasswordDigest="{b64encode(b_digest).decode()}", Nonce="{b64encode(b_nonce).decode()}", Created="{created}"'
```

hatena_photo_life.py

```python
class HatenaPhotoLife:
    def __init__(self, headers:dict=None):
        self.__headers = headers if headers else {}
        self.__base_url = 'https://f.hatena.ne.jp/atom'
    def post(self): pass
    def set_title(self): pass
    def delete(self): pass
    def get(self): pass
    def feed(self): pass
    @property
    def PostUri(self): return f'{self.__base_url}/post'
    @property
    def EditUri(self): return f'{self.__base_url}/edit'
    @property
    def FeedUri(self): return f'{self.__base_url}/feed'
```
```python
    def post(self, path:str, title:str=None, folder:str=None, generator:str=None):
        return requests.post(self.PostUri, data=data, headers=self.__headers)
```
```python
    def set_title(self, image_id:str, title:str):
        return requests.put(f'{self.EditUri}/{image_id}', data=data, headers=self.__headers)
```
```python
    def delete(self, image_id:str):
        return requests.delete(f'{self.EditUri}/{image_id}', headers=self.__headers)
```
```python
    def get(self, image_id:str):
        return requests.get(f'{self.EditUri}/{image_id}', headers=self.__headers)
```
```python
    def feed(self):
        return requests.get(self.FeedUri, headers=self.__headers)
```
```python
```
```python
```
```python
```
```python
```
```python
```
```python
```
```python
```
```python
```
