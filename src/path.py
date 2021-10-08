#!/usr/bin/env python3
# coding: utf8
# https://github.com/ytyaru/Python.Path.20210822091354
import os, sys, pathlib, csv, json, datetime, locale, inspect
from string import Template
from collections import namedtuple
class Path:
    @property
    def This(self): return str(pathlib.Path(inspect.stack()[1].filename).resolve())
    @property
    def Here(self): return str(pathlib.Path(inspect.stack()[1].filename).parent.resolve())
    @property
    def Current(self): return str(pathlib.Path(os.getcwd()).resolve())
    @Current.setter
    def Current(self, v): os.chdir(v)
    @property
    def Name(self): return str(pathlib.Path(inspect.stack()[1].filename).resolve().name)
    @property
    def Stem(self): return str(pathlib.Path(inspect.stack()[1].filename).resolve().stem)
    @property
    def Ext(self): return str(pathlib.Path(inspect.stack()[1].filename).resolve().suffix)
    @property
    def Parts(self): return list(pathlib.Path(inspect.stack()[1].filename).resolve().parts)
    @property
    def Depth(self): return len(self.Parts)

    def here(self, path): return str(pathlib.Path(pathlib.Path(inspect.stack()[1].filename).parent, '' if path is None else path.lstrip('/')).resolve())
    def current(self, path): return str(pathlib.Path(pathlib.Path(os.getcwd()), '' if path is None else path.lstrip('/')).resolve())
    def depth(self, path):
        if path is None or '' == path: return len(pathlib.Path(inspect.stack()[1].filename).parts)
        p = path if os.path.isabs(path) else pathlib.Path(pathlib.Path(inspect.stack()[1].filename).parent, path)
        return len(pathlib.Path(p).resolve().parts)
    def here_parent(self, num=1): return self.parent(self.Here, num)
    def current_parent(self, num=1): return self.parent(os.getcwd(), num)
    def parent(self, path, num=1):
        if num < 1: raise ValueError(f'遡る階層数は1以上の自然数にしてください。num={num}')
        p = pathlib.Path(path).resolve()
        if len(p.parts) <= num: raise ValueError(f'遡る階層数が多すぎます。引数numの値は{len(p.parts)-1}までです。{str(p)}')
        return str(p if num < 1 else p.parents[num - 1])
    def name(self, path):
        if path is None or '' == path: return pathlib.Path(inspect.stack()[1].filename).name
        return pathlib.Path(path).resolve().name
    def stem(self, path):
        if path is None or '' == path: return pathlib.Path(inspect.stack()[1].filename).stem
        return pathlib.Path(path).resolve().stem
    def ext(self, path):
        if path is None or '' == path: return pathlib.Path(inspect.stack()[1].filename).suffix
        return pathlib.Path(path).resolve().suffix
Path = Path()
