# From: https://github.com/pallets/flask

import sys
import os

basedir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, basedir + '/../')

from app import app
