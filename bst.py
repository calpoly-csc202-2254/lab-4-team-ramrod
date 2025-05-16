import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)


def comes_before(a: Any, b: Any) -> bool:
    return a < b

def example_fun(x : int) -> bool:
    return x < 142




class Tests(unittest.TestCase):
    pass

if (__name__ == '__main__'):
    unittest.main()