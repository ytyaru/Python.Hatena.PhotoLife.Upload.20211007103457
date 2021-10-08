#!/usr/bin/env python3
# coding: utf8
import os, sys
from unittest import TestLoader
from unittest import TextTestRunner
if __name__ == '__main__':
    TextTestRunner().run(TestLoader().discover(os.path.abspath(os.path.dirname(__file__))))
