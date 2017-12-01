#!/usr/bin/env python

'''
TreeOne.py 是学习二叉树时候所写的文件
TreeTwo.py 是复习二叉树所写的, 对应 https://git.io/vH0UP
'''

class TreeError(Exception):
    def __init__(self, msg):
        self._msg = msg

    def info(self):
        return self._msg

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.lc = None
        self.rc = None

class MyTree():
    def __init__(self):
        self.root = None
    
    def insert(self, root, val):
        '''
        使用递归
        '''
        if root == None:
            root = TreeNode(val)
            # return root # 在这里只能返回最后添加的节点到它上一层
        else:
            if val < root.val:
                root.lc = self.insert(root.lc, val)
            elif val > root.val:
                root.rc = self.insert(root.rc, val)
            else:
                raise TreeError("Exist same key")
        return root # 必须在这里继续返回, 否则这个函数默认返回None, 会将中间递归过程的节点置为None
    
    def insert_norec(self, root, val):
        if root == None: 
            root = TreeNode(val)
        while root != None:
            if val < root.val:
                if root.lc == None:
                    root.lc = TreeNode(val)
                    break 
                else:
                    root = root.lc
            if val > root.val:
                if root.rc == None:
                    root.rc = TreeNode(val)
                    break
                else:
                    root = root.rc
            else:
                raise TreeError("Exist same key")
        return root
    
    def pre_order(self, root, order_list):
        '''
        使用递归
        '''
        if root == None:
            return None
        
        order_list.append(root.val)
        self.pre_order(root.lc, order_list)
        self.pre_order(root.rc, order_list)
    
    def pre_order_norec(self, root, order_list):
        '''
        非递归版本
        '''
        stack = [root]
        cur = None
        while len(stack) != 0:
            cur = stack.pop()
            if cur.rc != None: stack.append(cur.rc)
            if cur.lc != None: stack.append(cur.lc)
            order_list.append(cur.val)
        
    def post_order(self, root, order_list):

        if root == None:
            return None

        self.post_order(root.lc, order_list)
        self.post_order(root.rc, order_list)
        order_list.append(root.val)


    def post_order_norec(self, root, order_list):
        stack1, stack2 = [root], []
        cur = None

        while len(stack1) != 0:
            cur = stack1.pop()
            stack2.append(cur)
            if cur.lc != None: stack1.append(cur.lc)
            if cur.rc != None: stack1.append(cur.rc)
        
        for i in stack2:
            order_list.append(i.val)
        order_list.reverse()
    
    def inner_order(self, root, order_list):
        
        if root == None:
            return None

        self.inner_order(root.lc, order_list)
        order_list.append(root.val)
        self.inner_order(root.rc, order_list)

    def inner_order_norec(self, root, order_list):
        '''
        1. 先依次将所有的左节点放入栈中
        2. 当到了最后一个左节点, 先检查该节点的左子节点, 发现为空, 然后弹出, 再检查其右子节点
        3. 如果右子节点不为空, 则将其当做一个新的树继续原来的操作
        4. 如果右子节点为空, 则可以用该条件弹出上面的父节点, 父节点弹出后再检查其右子节点
        '''
        stack = []
        cur = root
        while len(stack) != 0 or cur != None:
            if cur != None:
                stack.append(cur)
                cur = cur.lc
            else:
                cur = stack.pop()
                order_list.append(cur.val)
                cur = cur.rc
    
    def level_order(self, root, order_list):
        '''
        \\上一层 最右的一个节点的右子节点必定是下一层的最右节点\\
        上面描述是有问题的, 因为如果上一层最右节点未必有子节点,但它左边的节点有子节点
        '''
        if root == None:
            return None

        from collections import deque
        que = deque()
        que.append(root)
        last = root
        nlast = None 
        if last.lc != None:
            nlast = last.lc
        elif last.rc != None:
            nlast = last.rc

        while len(que) != 0:
            cur = que.popleft()
            order_list.append(cur.val)
            if cur.lc != None: 
                que.append(cur.lc)
                nlast = cur.lc
            if cur.rc != None: 
                que.append(cur.rc)
                nlast = cur.rc
            if cur == last:
                order_list.append('')
                last = nlast
            
    
    def find_min(self, root):
        while root.lc != None:
            root = root.lc
        return root.val
    
    def find_min_node(self, root):
        while root.lc != None:
            root = root.lc
        return root
    
    def find_max(self, root):
        while root.rc != None:
            root = root.rc
        return root.val
    
    def find_height(self, root):
        if root == None:
            return -1
        left_height = self.find_height(root.lc)
        right_height = self.find_height(root.rc)
        return max(left_height, right_height) + 1

    def is_binary_search_tree_fail(self, root):
        '''
        有缺陷的算法
        如果子书是BST, 但子书中有元素大于父节点, 则不为BST,本算法未能处理该状况
        '''
        left, right = False, False
        if root.lc == None and root.rc == None:
            return True
        # elif root.lc != None:
        if root.lc != None:
            if root.lc.val >= root.val:
                return False
            else:
                left = self.is_binary_search_tree(root.lc)
        else:
            left = True
        # elif root.rc != None: 
        # elif 语句不能用于不同变量的判断, 本代码逻辑是先处理root.lc,再处理rc, 
        # 但用了elif, 在lc判断为真的情况不会继续rc的判断
        if root.rc != None:
            if root.rc.val <= root.val:
                return False
            else:
                right = self.is_binary_search_tree(root.rc)
        else:
            right = True

        if left == True and right == True:
            return True
        
        return False
    
    def check_subtree(self, val, root, cmp):
        
        if root == None:
            return True
            
        left_lesser = self.check_subtree(val, root.lc, cmp)
        right_lesser = self.check_subtree(val, root.rc, cmp)

        if cmp(val, root.val) and left_lesser and right_lesser:
            return True
        else:
            return False
        
    def is_binary_search_tree(self, root):

        if root == None :
            return True

        left_bst = self.is_binary_search_tree(root.lc)
        left_lesser = self.check_subtree(root.val, root.lc, lambda x, y: x > y)
        right_bst = self.is_binary_search_tree(root.rc)
        right_greater = self.check_subtree(root.val, root.rc, lambda x, y: x < y)

        if left_bst and left_lesser and right_bst and right_greater:
            return True
        else:
            return False
    
    def is_bst_util(self, root, min_val, max_val):

        if root == None:
            return True

        left_bst = self.is_bst_util(root.lc, min_val, root.val)
        right_bst = self.is_bst_util(root.rc, root.val, max_val)

        if root.val > min_val and root.val < max_val and left_bst and right_bst:
            return True
        else:
            return False

    def is_binary_search_tree2(self, root):
        
        return self.is_bst_util(root, float('-inf'), float('inf'))
    
    def delete_node(self, val):
        '''
        上面所列的函数都不是很规范, 因为是递归, 直接调用还需要外部传入根节点
        所以应该封装多一层, 这样外部代码就不需要获取树的根节点了
        '''
        self.root = self.delete_node_help(self.root, val)
        return self.root
    
    def delete_node_help(self, root, val):
        if root == None:
            return root
        elif val < root.val:
            root.lc = self.delete_node_help(root.lc, val)
        elif val > root.val:
            root.rc = self.delete_node_help(root.rc, val)
        else:
            # case 1 相等节点有 0 个子节点
            if root.lc == None and root.rc == None:
                root = None

            # case 2 相等节点有一个子节点树
            elif root.lc == None:
                root = root.rc
            elif root.rc == None:
                root = root.lc
            
            # case 3 相等节点有两个子节点树
            else:
                temp = self.find_min_node(root.rc)
                root.val = temp.val
                root.rc = self.delete_node_help(root.rc, temp.val)      

        return root

