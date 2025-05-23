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
    comes_before: Callable[[Any,Any],bool]
    tree: BinTree


#checks to see if a frozenBinarySearchTree is empty
def is_empty(fbst:frozenBinarySearchTree)-> bool:
    if fbst.tree == None:
        return True
    else: return False

 # inserts a value into a frozen binary search tree according to the order defined by comes_before   
def insert(fbst:frozenBinarySearchTree,val:Any)->frozenBinarySearchTree:
    bin = insert_helper(fbst.tree,val,fbst.comes_before)
    return frozenBinarySearchTree(fbst.comes_before,bin)

def insert_helper(bt:BinTree,val:Any,function:Callable[[Any,Any],bool])->BinTree:
    match bt:
        case None:
            return Node(val,None,None)
        case Node(v,l,r):
            if function(val,v):
                return Node(v,insert_helper(l,val,function),r)
            else: return Node(v,l,insert_helper(r,val,function))
    
#returns true if value is stored in tree
def lookup(fbst:frozenBinarySearchTree,val:Any)->bool:
    return lookup_helper(fbst.comes_before,fbst.tree,val)

def lookup_helper(function:Callable[[Any,Any],bool],bt:BinTree,val:Any)->bool:
    match bt:
        case None:
            return False
        case Node(v,l,r):
            if not function(val,v) and not function(v,val):
                return True
            elif function(val,v): 
                return lookup_helper(function,l,val) 
            else: return lookup_helper(function,r,val)

#given a bst and a value, value is removed from the tree, and keeps the order correct
def delete(fbst:frozenBinarySearchTree,val:Any)->frozenBinarySearchTree:
    bin = delete_helper(fbst.comes_before,fbst.tree,val)
    return frozenBinarySearchTree(fbst.comes_before,bin)

def delete_helper(function:Callable[[Any,Any],bool],bt:BinTree,val:Any)->BinTree:
    match bt:
        case None:
            return None
        case Node(v,l,r):
            if not function(val,v) and not function(v,val):
                match (l,r):
                    case (None,None):
                        return None
                    case (None,_):
                        return r
                    case (_,None):
                        return l
                    case (_,_):
                        replacement = find_min(r)
                        new_r = delete_helper(function,r,replacement)
                        return Node(replacement, l, new_r)
            elif function(val,v):
                return Node(v,delete_helper(function,l,val),r)
            else: return Node(v,l,delete_helper(function,r,val))

def find_min(bt:BinTree)->Any:
    if bt is None:
        raise ValueError("Cannot find min of an empty tree")
    if bt.left == None:
        return bt.val
    else: return find_min(bt.left)

             
                 

def example_fun(x : int) -> bool:
    return x < 142

def comes_before(a:Any,b:Any)->bool:
    return a < b


class Tests(unittest.TestCase):
    def test_is_empty(self):
        
        tree:BinTree = Node(5,None,None)
        fbst:frozenBinarySearchTree = frozenBinarySearchTree(comes_before,None)
        fbst1:frozenBinarySearchTree = frozenBinarySearchTree(comes_before,tree)
        self.assertEqual(True,is_empty(fbst))
        self.assertEqual(False,is_empty(fbst1))

    def test_insert(self):
        tree:BinTree = Node(5,None,None)
        fbst:frozenBinarySearchTree = frozenBinarySearchTree(comes_before,tree)
        tree2:BinTree = Node(5,Node(4,None,None),None)
        expected = frozenBinarySearchTree(comes_before,tree2)
        self.assertEqual(expected,insert(fbst,4))

    def test_lookup(self):
        tree:BinTree = Node(5,None,None)
        tree2:BinTree = Node(5,Node(4,None,None),None)
        fbst:frozenBinarySearchTree = frozenBinarySearchTree(comes_before,tree)
        fbst2:frozenBinarySearchTree = frozenBinarySearchTree(comes_before,tree2)
        self.assertEqual(True,lookup(fbst,5))
        self.assertEqual(True,lookup(fbst2,4))
        self.assertEqual(False,lookup(fbst2,1))

    def test_find_min(self):
        tree:BinTree = Node(5,Node(4,None,None),None)
        self.assertEqual(4,find_min(tree))

    def test_delete(self):
        tree2:BinTree = Node(5,Node(4,None,None),None)
        fbst2:frozenBinarySearchTree = frozenBinarySearchTree(comes_before,tree2)
        expected_BinTree:BinTree = Node(4,None,None)
        expected:frozenBinarySearchTree = frozenBinarySearchTree(comes_before,expected_BinTree)
        self.assertEqual(expected,delete(fbst2,5))



if (__name__ == '__main__'):
    unittest.main()