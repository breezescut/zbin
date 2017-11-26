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
        try:
            if parent is None:
                # print('newOne:{}, parent:{}, self._root:{}'.format(newOne, id(parent), id(self._root)))
                newNode = TreeNode(newOne)
                parent = newNode
                self._nodeNum += 1
                # print('newOne:{}, parent:{}, self._root:{}'.format(newOne, id(parent), id(self._root)))
                return parent
            elif newOne < parent.get_val():
                # print("LC Parent:{}".format(parent.get_val()))
                child = self.insert(parent.get_lc(), newOne)
                if child is not None: parent.add_leftChild(child)
                # print("LC:{}".format(parent._lc.get_val()))
            elif newOne > parent.get_val():
                # print("RC Parent:{}".format(parent.get_val()))
                child = self.insert(parent.get_rc(), newOne)
                if child is not None: parent.add_rightChild(child)
                # print("RC:{}".format(parent._rc.get_val()))
            else:
                raise TreeError("key exist")
        except TreeError as ex:
            print(ex.info())

    def pre_order(self, node, order_list):
        if node == None: return
        # print(node.get_val())
        order_list.append(node.get_val())
        self.pre_order(node.get_lc(), order_list)
        self.pre_order(node.get_rc(), order_list)
        
    def post_order(self, node, order_list):
        if node == None: return 
        self.post_order(node.get_lc(), order_list)
        self.post_order(node.get_rc(), order_list)
        order_list.append(node.get_val())
    
    def inner_order(self, node, order_list):
        if node == None: return
        self.inner_order(node.get_lc(), order_list)
        order_list.append(node.get_val())
        self.inner_order(node.get_rc(), order_list)