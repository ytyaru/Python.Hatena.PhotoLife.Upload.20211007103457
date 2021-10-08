#!/usr/bin/env python3
# coding: utf8
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

