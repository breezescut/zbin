#!/usr/bin/env python

import unittest
from TreeOne import MyTree, TreeNode

class TestTreeOne(unittest.TestCase):
    
    def testOne(self):
        lt = [123,2,34,324,235,45,435,1432,342,42]
        
        mtree = MyTree()
        for i in lt:
            root = mtree.get_root()
            newRoot = mtree.insert3(root, i)
            if root is None: mtree.set_root(newRoot)
            root2 = mtree.get_root()
        
        pre_list = []
        mtree.pre_order(mtree.get_root(), pre_list)
        pre_list2 = []
        mtree.pre_order_norec(mtree.get_root(), pre_list2)
        print('pre_order:', pre_list, pre_list2)
        for i in range(len(pre_list)):
            self.assertEqual(pre_list[i], pre_list2[i])

        post_list, post_list2 = [], []
        mtree.post_order(mtree.get_root(), post_list)
        mtree.post_order_norec(mtree.get_root(), post_list2)
        print('post_order:', post_list, post_list2)

        inner_list, inner_list2 = [], []
        mtree.inner_order(mtree.get_root(), inner_list)
        mtree.inner_order_norec(mtree.get_root(), inner_list2)
        print('innner_order:', inner_list, inner_list2)

        level_list = []
        mtree.level_order(mtree.get_root(), level_list)
        print('level_list:', level_list)

        level_list2 = []
        mtree.level_order2(mtree.get_root(), level_list2)
        print('level_list2:', level_list2)
        # for i in level_list2:
        #     print(i, end=' ')
        
        spre_lt = []
        mtree.serialize_pre_order(mtree.get_root(), spre_lt)
        print('serialize_pre:', spre_lt)

        xmin = mtree.find_min()
        print("min:", xmin)
        xmax = mtree.find_max()
        print('max:', xmax)

        print('mtree height:', mtree.find_height(mtree.get_root()))
        

if __name__ == '__main__':
    unittest.main()

