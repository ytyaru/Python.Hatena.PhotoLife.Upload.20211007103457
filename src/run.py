#!/usr/bin/env python3
# coding: utf8
import os, sys
import json
import jsonschema 
import argparse
import xmltodict
import path
#from WSSE import wsse
#from HatenaPhotoLife import hatena_photo_life
from wsse import WSSE 
from hatena_photo_life import HatenaPhotoLife
VERSION='0.0.1'
class FileReader:
    @classmethod
    def text(self, path):
        with open(path, mode='r', encoding='utf-8') as f: return f.read().rstrip('\n')
    @classmethod
    def json(self, path):
        with open(path, mode='r', encoding='utf-8') as f: return json.load(f)

def parse_command_by_argparse():
    parser = argparse.ArgumentParser(description=f'画像をアップロードする。はてなフォトライフへ。	{VERSION}')
    parser.add_argument('path', help='画像ファイルパス')
    parser.add_argument('-t', '--title', help='画像のタイトル（初期値＝pathのファイル名）')
    parser.add_argument('-f', '--folder', help='アップロード先のフォルダ名')
    parser.add_argument('-g', '--generator', help='アップロードしたツール名（フォルダ振分用）')
    parser.add_argument('-p', '--response-parser', help='API応答パーサのパス（LinedResponseParser.py）')
#    parser.add_argument('-p', '--not-parse-response', action='store_true', help='API応答をパースせず全XMLを出力する。デフォルトでは以下3つを1行おきに出力する。hatena:imageurl, hatena:imageurlsmall, hatena:syntax', type=bool, default=False)
#   parser.add_argument('-o', '--output-format', help='出力形式', default='text', choices=['text', 'xml'])
    args = parser.parse_args()
    print(args)
    return args

def parse_response(res):
    xml = xmltodict.parse(res.text)
#    print(xml['entry']['dc:subject']['#text'])
#    print(xml['entry']['generator']['#text'])
    print(xml['entry']['hatena:imageurl'])
    print(xml['entry']['hatena:imageurlsmall'])
    print(xml['entry']['hatena:syntax'])
    
def test_xml():
    xml = xmltodict.parse(FileReader.json(Path.here('test-3.xml')))
    print(xml)
    print(xml['entry']['dc:subject']['#text'])
    print(xml['entry']['generator']['#text'])
    print(xml['entry']['hatena:imageurl'])
    print(xml['entry']['hatena:imageurlsmall'])
    print(xml['entry']['hatena:syntax'])
#    with open('test.xml', 'r', encoding='utf-8') as f:
#        xml = xmltodict.parse(f.read())
#        print(xml)
#if __name__ == '__main__':
#    main()
#    valid_secret()
if __name__ == '__main__':
    # コマンド解析
    args = parse_command_by_argparse()
    sys.exit(1)
    # APIクライアント生成
    api = HatenaPhotoLife(
            WSSE.from_json(
                FileReader.json(Path.here('secret.json')),
                FileReader.json(Path.here('secret-schema.json'))))
    # リクエスト
    res = api.post(args.path, title=args.title, folder=args.folder, generator=args.generator) 
    if res.ok:
        # レスポンスをパースする
        parse_response(res)
    else:
        # エラーを表示する
        print('[ERROR] リクエストに失敗しました。HTTPステータスコードが200〜400以外です。', file=sys.stderr)
        print(res.status_code, file=sys.stderr)
        print(res.text, file=sys.stderr)
        res.raise_for_status()


