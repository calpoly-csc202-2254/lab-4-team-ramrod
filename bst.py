import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

BinTree: TypeAlias = Union[None,"Node"]

@dataclass(frozen=True)
class Node:
    val: Any
    left: BinTree
    right: BinTree

@dataclass(frozen=True)
class frozenBinarySearchTree:
    Tree: BinTree
    comes_before: Callable[[Node,Node],bool]


def is_empty(fbst:frozenBinarySearchTree)-> bool:
    if fbst.Tree == None:
        return True
    else: return False
    
def insert(fbst:frozenBinarySearchTree,val:Any)->frozenBinarySearchTree:
    bin = insert_helper(fbst.Tree,val,fbst.comes_before)
    return frozenBinarySearchTree(bin,fbst.comes_before)

def insert_helper(bt:BinTree,val:Any,function:Callable[[Node,Node],bool])->BinTree:
    match bt:
        case None:
            return None
        case Node(v,l,r):
            if function(v,val):
                return insert_helper(r)
            else: return insert_helper(l)




def example_fun(x : int) -> bool:
    return x < 142




class Tests(unittest.TestCase):
    pass

if (__name__ == '__main__'):
    unittest.main()