import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

from bst import *

def numeric_ordering(a:int,b:int)->bool:
    return a < b

def alphabetic_ordering(a:str,b:str)->bool:
    return str(a) < str(b)

def euclidean_ordering(point1:tuple[int,int],point2:tuple[int,int])->bool:
    return (point1[0]**2 + point1[1]**2)<(point2[0]**2 + point2[1]**2)

class BSTTests(unittest.TestCase):
    def test_example_fun(self):
        self.assertEqual(True, example_fun(34))
        self.assertEqual(False,example_fun(1423))
    def test_numeric_ordering(self):
        tree:BinTree = Node(13,Node(4,None,None),Node(17,None,None))
        fbst = frozenBinarySearchTree(numeric_ordering,tree)
        fbst2 = frozenBinarySearchTree(numeric_ordering,None)
        fbst2 = insert(fbst2,13)
        fbst2 = insert(fbst2,4)
        fbst2 = insert(fbst2,17)
        self.assertEqual(fbst,fbst2)
    
    def test_alphabetic_ordering(self):
        tree:BinTree = Node("banana",Node("apple",None,None),Node("cucumber",None,None))
        fbst = frozenBinarySearchTree(alphabetic_ordering,tree)
        fbst2 = frozenBinarySearchTree(alphabetic_ordering,None)
        fbst2 = insert(fbst2,"banana")
        fbst2 = insert(fbst2,"apple")
        fbst2 = insert(fbst2,"cucumber")
        self.assertEqual(fbst,fbst2)

    def test_euclidean_ordering(self):
        point1 = Tuple[1,1]
        point2 = Tuple[1,3]
        point3 = Tuple[1,2]

        tree:BinTree = Node(point1,None,Node(point2,Node(point3,None,None),None))
        fbst = frozenBinarySearchTree(alphabetic_ordering,tree)
        fbst2 = frozenBinarySearchTree(alphabetic_ordering,None)
        fbst2 = insert(fbst2,point1)
        fbst2 = insert(fbst2,point2)
        fbst2 = insert(fbst2,point3)
        self.assertEqual(fbst,fbst2)


    

if (__name__ == '__main__'):
    unittest.main()
