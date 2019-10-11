# -*- coding: UTF-8 -*-

import os

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.join(CURRENT_DIR, '..')

def base_path(path=''):
    return os.path.join(BASE_DIR, path)
