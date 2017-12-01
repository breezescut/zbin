import unittest
from TreeTwo import MyTree, TreeNode

class TestTreeTwo(unittest.TestCase):

    def setUp(self):
        self.mtree = MyTree()
        lt = [123,2,34,324,235,45,435,1432,342,42]
        for i in lt:
            self.mtree.root = self.mtree.insert(self.mtree.root, i)

    def test_preOrder(self):
        mtree = self.mtree
        
        pre_list1 = []
        mtree.pre_order(mtree.root, pre_list1)
        pre_list2 = []
        mtree.pre_order_norec(mtree.root, pre_list2)
        self.assertEqual(pre_list1, pre_list2)
        # print(pre_list2)
    
    def test_postOrder(self):
        mtree = self.mtree

        post_list1 = []
        mtree.post_order(mtree.root, post_list1)
        post_list2 = []
        mtree.post_order_norec(mtree.root, post_list2)
        self.assertEqual(post_list1, post_list2)
    
    def test_innerOrder(self):
        mtree = self.mtree

        inn_list1 = []
        mtree.inner_order(mtree.root, inn_list1)
        inn_list2 = []
        mtree.inner_order_norec(mtree.root, inn_list2)
        self.assertEqual(inn_list1, inn_list2)
    
    def test_levelOrder(self):
        mtree = self.mtree

        level_list = []
        mtree.level_order(mtree.root, level_list)

        # print(level_list)
    
    def test_findMin(self):
        pass
    
    def test_is_binary_search_tree(self):
        mtree = self.mtree

        self.assertTrue(mtree.is_binary_search_tree2(mtree.root))

        mtree2 = MyTree()
        mtree2.root = TreeNode(5)
        mtree2.root.lc = TreeNode(7)
        mtree2.root.rc = TreeNode(3)
        x_node = mtree2.root.lc
        x_node.lc = TreeNode(67886)
        x_node.rc = TreeNode(-22)
        x_node = mtree2.root.rc
        x_node.lc = TreeNode(32432434)
        x_node.rc = TreeNode(-17878123)

        order_list = []
        mtree2.level_order(mtree2.root, order_list)
        # print(order_list)

        self.assertFalse(mtree2.is_binary_search_tree2(mtree2.root))

        mtree3 = MyTree()
        lt = [10, 5, 16, 7,4,1]
        for i in lt:
            mtree3.root = mtree3.insert(mtree3.root, i)
        mtree3.root.lc.rc.rc = TreeNode(11)
        
        # level_order = []
        # mtree3.level_order(mtree3.root, level_order)
        # print('mtree3:{}'.format(level_order))

        # inn_order = []
        # mtree3.inner_order(mtree3.root, inn_order)
        # print('inn_order:{}'.format(inn_order))

        self.assertFalse(mtree3.is_binary_search_tree2(mtree3.root))
        self.assertTrue(mtree3.is_binary_search_tree_fail(mtree3.root))
    
    def test_del_node(self):
        mtree = MyTree()
        lt = [123,2,34,324,235,45,435,1432,342,42]
        for i in lt:
            mtree.root = mtree.insert(mtree.root, i)
        # case 0 无
        # result = mtree.delete_node(43)
        # level_list = []
        # mtree.level_order(result, level_list)
        # print(level_list)
        
        # case 1
        result = mtree.delete_node(435)
        level_list2 = []
        mtree.level_order(result, level_list2)
        print(level_list2)




if __name__ == '__main__':
    unittest.main()