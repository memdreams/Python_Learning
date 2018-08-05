# nose is similar to unittest
from nose.tools import *
import VIDEODOWNLOAD

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN.")
