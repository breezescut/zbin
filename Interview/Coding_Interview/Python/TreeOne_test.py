#!/usr/bin/env python

import unittest
from TreeOne import MyTree, TreeNode

class TestTreeOne(unittest.TestCase):
    
    def testOne(self):
        lt = [123,2,34,324,235,45,435,1432,342,42]
        
        mtree = MyTree()
        for i in lt:
            root = mtree.get_root()
            # mtree.set_root(mtree.insert(root, i))
            # print("start insert")
            newRoot = mtree.insert(root, i)
            # print("end insert")
            # print("newRoot:{}".format(newRoot.get_val()))
            if root is None: mtree.set_root(newRoot)
            root2 = mtree.get_root()
            # print("root2:{}".format(root2.get_val()))
            # print("root2:{}".format(id(root2)))
            # print("\n"*2)
        
        pre_list = []
        mtree.pre_order(mtree.get_root(), pre_list)
        print(pre_list)
        post_list = []
        mtree.post_order(mtree.get_root(), post_list)
        print(post_list)
        inner_list = []
        mtree.inner_order(mtree.get_root(), inner_list)
        print(inner_list)
    

if __name__ == '__main__':
    unittest.main()

