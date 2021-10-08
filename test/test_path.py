#!/usr/bin/env python3
# coding: utf8
import os,sys,pathlib,inspect
sys.path.append(str(pathlib.Path(__file__, '../../src').resolve()))
from path import Path
import unittest
class TestPath(unittest.TestCase):
    def test_This(self): self.assertEqual(Path.This, __file__)
    def test_Here(self): self.assertEqual(Path.Here, os.path.dirname(__file__))
    def test_Current_get(self): self.assertEqual(Path.Current, os.getcwd())
    def test_Current_set(self):
        expected = os.path.expanduser("~")
        Path.Current = expected 
        self.assertEqual(Path.Current, expected)
    def test_Name(self): self.assertEqual(Path.Name, os.path.basename(__file__))
    def test_Stem(self): self.assertEqual(Path.Stem, os.path.splitext(os.path.basename(__file__))[-2])
    def test_Ext(self): self.assertEqual(Path.Ext, os.path.splitext(os.path.basename(__file__))[-1])
    def test_Parts(self): self.assertEqual(Path.Parts, list(pathlib.Path(__file__).resolve().parts))
    def test_Depth(self): self.assertEqual(Path.Depth, len(list(pathlib.Path(__file__).resolve().parts)))
    def test_here_brother_0(self): self.assertEqual(Path.here('a.txt'), str(pathlib.Path(__file__, '../a.txt').resolve()))
    def test_here_brother_1(self): self.assertEqual(Path.here('./a.txt'), str(pathlib.Path(__file__, '../a.txt').resolve()))
    def test_here_parent(self): self.assertEqual(Path.here('../a.txt'), str(pathlib.Path(__file__, '../../a.txt').resolve()))
    def test_here_child(self): self.assertEqual(Path.here('some/a.txt'), str(pathlib.Path(__file__, '../some/a.txt').resolve()))
    def test_here_abs(self): self.assertEqual(Path.here('/some/a.txt'), str(pathlib.Path(__file__, '../some/a.txt').resolve()))
    def test_here_last_slash(self): self.assertEqual(Path.here('/some/a.txt/'), str(pathlib.Path(__file__, '../some/a.txt').resolve()))
    def test_here_empty(self): self.assertEqual(Path.here(''), os.path.dirname(__file__))
    def test_here_none(self): self.assertEqual(Path.here(None), os.path.dirname(__file__))

    def test_current_brother_0(self): self.assertEqual(Path.current('a.txt'), str(pathlib.Path(os.getcwd(), 'a.txt').resolve()))
    def test_current_brother_1(self): self.assertEqual(Path.current('./a.txt'), str(pathlib.Path(os.getcwd(), 'a.txt').resolve()))
    def test_current_parent(self): self.assertEqual(Path.current('../a.txt'), str(pathlib.Path(os.getcwd(), '../a.txt').resolve()))
    def test_current_child(self): self.assertEqual(Path.current('some/a.txt'), str(pathlib.Path(os.getcwd(), 'some/a.txt').resolve()))
    def test_current_abs(self): self.assertEqual(Path.current('/some/a.txt'), str(pathlib.Path(os.getcwd(), 'some/a.txt').resolve()))
    def test_current_last_slash(self): self.assertEqual(Path.current('/some/a.txt/'), str(pathlib.Path(os.getcwd(), 'some/a.txt').resolve()))
    def test_current_empty(self): self.assertEqual(Path.current(''), os.getcwd())
    def test_current_none(self): self.assertEqual(Path.current(None), os.getcwd())

    def test_here_parent(self): self.assertEqual(Path.here_parent(), str(pathlib.Path(Path.Here).parent))
    def test_here_parent_one(self): self.assertEqual(Path.here_parent(1), str(pathlib.Path(Path.Here).parent))
    def test_here_parent_two(self): self.assertEqual(Path.here_parent(2), str(pathlib.Path(Path.Here).parent.parent))
    def test_here_parent_zero(self):
        with self.assertRaises(ValueError, msg='遡る階層数は1以上の自然数にしてください。'):
            Path.here_parent(0)
    def test_here_parent_over(self):
        with self.assertRaises(ValueError, msg='遡る階層数が多すぎます。'):
            Path.here_parent(Path.Depth-1)

    def test_current_parent(self): self.assertEqual(Path.current_parent(), str(pathlib.Path(Path.Current).parent))
    def test_current_parent_one(self): self.assertEqual(Path.current_parent(1), str(pathlib.Path(Path.Current).parent))
    def test_current_parent_two(self): self.assertEqual(Path.current_parent(2), str(pathlib.Path(Path.Current).parent.parent))
    def test_current_parent_zero(self):
        with self.assertRaises(ValueError, msg='遡る階層数は1以上の自然数にしてください。'):
            Path.current_parent(0)
    def test_current_parent_over(self):
        with self.assertRaises(ValueError, msg='遡る階層数が多すぎます。'):
            Path.current_parent(Path.Depth-1)

    def test_parent(self): self.assertEqual(Path.parent(__file__), str(pathlib.Path(__file__).parent))
    def test_parent_one(self): self.assertEqual(Path.parent(__file__, 1), str(pathlib.Path(__file__).parent))
    def test_parent_two(self): self.assertEqual(Path.parent(__file__, 2), str(pathlib.Path(__file__).parent.parent))
    def test_parent_zero(self):
        with self.assertRaises(ValueError, msg='遡る階層数は1以上の自然数にしてください。'):
            Path.parent(__file__, 0)
    def test_parent_over(self):
        with self.assertRaises(ValueError, msg='遡る階層数が多すぎます。'):
            Path.parent(__file__, Path.Depth)
    def test_parent_not_pathlike(self):
        with self.assertRaises(TypeError, msg='expected str, bytes or os.PathLike object, not int'):
            Path.parent(0)

    def test_depth_dir(self): self.assertEqual(Path.depth('/tmp'), 2)
    def test_depth_dir_file(self): self.assertEqual(Path.depth('/tmp/a.txt'), 3)
    def test_depth_rel_path(self): self.assertEqual(Path.depth('/tmp/work/../a.txt'), 3)
    def test_depth_rel_path_name_0(self): self.assertEqual(Path.depth('a.txt'), len(pathlib.Path(__file__, '../a.txt').resolve().parts))
    def test_depth_rel_path_name_1(self): self.assertEqual(Path.depth('./a.txt'), len(pathlib.Path(__file__, '../a.txt').resolve().parts))
    def test_depth_rel_path_name_2(self): self.assertEqual(Path.depth('../a.txt'), len(pathlib.Path(__file__, '../../a.txt').resolve().parts))
    def test_depth_empty(self): self.assertEqual(Path.depth(''), len(pathlib.Path(__file__).resolve().parts))
    def test_depth_none(self): self.assertEqual(Path.depth(None), len(pathlib.Path(__file__).resolve().parts))

    def test_name_empty(self): self.assertEqual(Path.name(''), os.path.basename(__file__))
    def test_name_none(self): self.assertEqual(Path.name(None), os.path.basename(__file__))
    def test_name_dir(self): self.assertEqual(Path.name('/tmp'), 'tmp')
    def test_name_dir_file(self): self.assertEqual(Path.name('/tmp/a.txt'), 'a.txt')
    def test_name_last_slash(self): self.assertEqual(Path.name('/tmp/a.txt/'), 'a.txt')
    def test_name_file_0(self): self.assertEqual(Path.name('a.txt'), 'a.txt')
    def test_name_file_1(self): self.assertEqual(Path.name('./a.txt'), 'a.txt')
    def test_name_file_2(self): self.assertEqual(Path.name('../a.txt'), 'a.txt')

    def test_stem_empty(self): self.assertEqual(Path.stem(''), os.path.splitext(os.path.basename(__file__))[0])
    def test_stem_none(self): self.assertEqual(Path.stem(None), os.path.splitext(os.path.basename(__file__))[0])
    def test_stem_dir(self): self.assertEqual(Path.stem('/tmp'), 'tmp')
    def test_stem_dir_file(self): self.assertEqual(Path.stem('/tmp/a.txt'), 'a')
    def test_stem_last_slash(self): self.assertEqual(Path.stem('/tmp/a.txt/'), 'a')
    def test_stem_file_0(self): self.assertEqual(Path.stem('a.txt'), 'a')
    def test_stem_file_1(self): self.assertEqual(Path.stem('./a.txt'), 'a')
    def test_stem_file_2(self): self.assertEqual(Path.stem('../a.txt'), 'a')

    def test_ext_empty(self): self.assertEqual(Path.ext(''), os.path.splitext(os.path.basename(__file__))[1])
    def test_ext_none(self): self.assertEqual(Path.ext(None), os.path.splitext(os.path.basename(__file__))[1])
    def test_ext_dir(self): self.assertEqual(Path.ext('/tmp'), '')
    def test_ext_dir_file(self): self.assertEqual(Path.ext('/tmp/a.txt'), '.txt')
    def test_ext_last_slash(self): self.assertEqual(Path.ext('/tmp/a.txt/'), '.txt')
    def test_ext_file_0(self): self.assertEqual(Path.ext('a.txt'), '.txt')
    def test_ext_file_1(self): self.assertEqual(Path.ext('./a.txt'), '.txt')
    def test_ext_file_2(self): self.assertEqual(Path.ext('../a.txt'), '.txt')

if __name__ == "__main__":
    unittest.main()
