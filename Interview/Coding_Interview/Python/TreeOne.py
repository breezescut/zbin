#!/usr/bin/env python

# from collections import Iterable
# from type_limit import type_limit


class TreeError(Exception):
    def __init__(self, msg):
        self._msg = msg

    def info(self):
        return self._msg


class TreeNode():
    def __init__(self, val):
        # 4 element: parent, lc, rc, val
        self._parent = None
        self._lc = None
        self._rc = None
        if not isinstance(val, (int, float)):
            raise TreeError("Tree node init val is not a number")
        else:
            self._val = val

    def set_parent(self, pa_node):
        self._parent = pa_node

    def get_parent(self):
        return self._parent

    def get_val(self):
        return self._val

    def add_leftChild(self, lc_node):
        self._lc = lc_node
        self._lc.set_parent(self)

    def add_rightChild(self, rc_node):
        self._rc = rc_node
        self._rc.set_parent(self)
    
    def get_lc(self):
        return self._lc
    
    def get_rc(self):
        return self._rc


class MyTree():
    def __init__(self):
        self._root = None
        self._nodeNum = 0
    
    def set_root(self, root):
        self._root = root

    def get_root(self):
        return self._root

    def insert(self, parent, newOne):
        if parent is None:
            parent = TreeNode(newOne)
            return parent
        elif newOne < parent.get_val():
            child = self.insert(parent.get_lc(), newOne)
            if child is not None:
                parent.add_leftChild(child)
        elif newOne > parent.get_val():
            child = self.insert(parent.get_rc(), newOne)
            if child is not None:
                parent.add_rightChild(child)
        else:
            raise TreeError("key exist")
    
    def insert2(self, head, val):
        if head is None:
            head = TreeNode(val)
        else:
            if val < head.get_val():
                head._lc = self.insert2(head.get_lc(), val)
            elif val > head.get_val():
                head._rc = self.insert2(head.get_rc(), val)
            else:
                raise TreeError("Same key exists")
        return head

    def insert3(self, head, val):
        '''
        无递归, 使用循环实现
        '''
        root = head
        if head == None: return TreeNode(val)
        while True:
            if val < head.get_val():
                if head._lc == None:
                    head._lc = TreeNode(val)
                    break
                else:
                    head = head._lc
            elif val > head.get_val():
                if head._rc == None:
                    head._rc = TreeNode(val)
                    break
                else:
                    head = head._rc
            else:
                raise TreeError("Same key exists")
        return root




    def pre_order(self, node, order_list):
        if node == None: return
        order_list.append(node.get_val())
        self.pre_order(node.get_lc(), order_list)
        self.pre_order(node.get_rc(), order_list)
    
    def pre_order_norec(self, node, order_list):
        '''
        非递归实现
        1. 先将头结点压入栈
        2. 循环开始,将栈首节点弹出
        3. 将弹出节点的子节点按右到左压入栈(非空子节点)
        4. 循环重复, 直到栈为空
        '''
        stack = [node]
        while len(stack) != 0:
            cur = stack.pop()
            rc, lc = cur.get_rc(), cur.get_lc()
            if rc is not None: stack.append(rc)
            if lc is not None: stack.append(lc)
            
            order_list.append(cur.get_val())
        
    def post_order(self, node, order_list):
        if node == None: return 
        self.post_order(node.get_lc(), order_list)
        self.post_order(node.get_rc(), order_list)
        order_list.append(node.get_val())
    
    def post_order_norec(self, node, order_list):
        '''
        后序和前序本质上是同一种算法, 前序是"中左右", 后序是"左右中"
        后序可转换为"中右左", 反序即可变后序
        而"中右左" 则是前序"中左右" 左右子书入栈顺序不同而已
        '''
        stack1, stack2 = [node], []
        while len(stack1) != 0:
           cur = stack1.pop()
           stack2.append(cur)
           rc, lc = cur.get_rc(), cur.get_lc()
           if lc != None: stack1.append(lc)
           if rc != None: stack1.append(rc)
        
        stack2.reverse()
        for i in stack2:
            order_list.append(i.get_val())
    
    def inner_order(self, node, order_list):
        if node == None: return
        self.inner_order(node.get_lc(), order_list)
        order_list.append(node.get_val())
        self.inner_order(node.get_rc(), order_list)

    def inner_order_norec(self, node, order_list):
        cur, stack = node.get_lc(), [node]
        while len(stack) != 0 or cur != None:
            if cur != None: 
                stack.append(cur)
                cur = cur.get_lc()
            else:
                cur = stack.pop()
                order_list.append(cur.get_val())
                cur = cur.get_rc()
    
    def level_order(self, node, order_list):
        from collections import deque
        que = deque()
        que.append(node)

        while len(que) != 0:
            cur = que.popleft()
            lc, rc = cur.get_lc(), cur.get_rc()
            if lc != None: que.append(lc)
            if rc != None: que.append(rc)
            order_list.append(cur.get_val())
        
    def level_order2(self, node, order_list):
        '''
        1. 使用两个变量 last 和 nlast, last 代表每层最右节点, nlast 跟踪每个压入队列的节点,
        2. 当last 指向节点被弹出后, 换行, 并将last 指向 nlast, nlast 继续跟踪后续压入队列的节点
        3. last 初始化为头节点, nlast 初始化为头节点的第一个非空子节点
        4. 当 last 指向的节点被弹出后, 代表下一层所有的节点都被压入队列, nlast 指向该层最后一个压入的节点
        '''
        from collections import deque
        que = deque()
        que.append(node)
        last = node
        nlast = None
        while len(que) != 0:
            cur = que.popleft()
            lc, rc = cur.get_lc(), cur.get_rc()
            if lc != None: 
                que.append(lc)
                nlast = lc
            if rc != None: 
                que.append(rc)
                nlast = rc
            order_list.append(cur.get_val())
            if last == cur: 
                order_list.append('\n')
                last = nlast

    def serialize_pre_order(self, node, order_list):
        if node == None: 
            order_list.append('#!')
            return
        order_list.append('{}!'.format(node.get_val()))
        self.serialize_pre_order(node.get_lc(), order_list)
        self.serialize_pre_order(node.get_rc(), order_list)
    
    def deserialize_pre_order(self, node, order_list):
        '''
        暂未想到实现思路
        '''
        pass
            
    def find_min(self):
        if self._root == None: return None
        node = self._root
        while node.get_lc() != None:
            node = node.get_lc()
        return node.get_val()
    
    def find_max(self):
        if self._root == None: return None
        node = self._root
        while node.get_rc() != None:
            node = node.get_rc()
        return node.get_val()
    
    def find_height(self, root):
        if root == None:
            return -1
        left_height = self.find_height(root._lc)
        right_height = self.find_height(root._rc)
        return max(left_height, right_height)+1