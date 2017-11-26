#!/usr/bin/env python

class ListError(Exception):
    def __init__(self, err_info):
        self._err = err_info
    
    def info(self):
        return self._err


class Node():
    def __init__(self, val=None):
        if val is None:
            self._element = object()
        else:
            self._element = val
        
        self._next = None

    def set_next(self, next_node):
        self._next = next_node
    
    def get_next(self):
        return self._next


    def get_val(self):
        return self._element

class Zlist():

    def __init__(self, it=None):
        self._head = None
        self._tail = None
        self._size = 0
        if it is not None:
            for i in it:
                node = Node(i)
                if self._head is None:
                    self._head = node
                    self._tail = node
                else:
                    self._tail.set_next(node)
                    self._tail = node
                self._size += 1
    
    def get_size(self):
        return self._size
    
    def empty(self):
        if self._size == 0:
            return True
        else:
            return False
    
    def value_at(self, index):
        if index < 0:
            index = self._size - index
        if index >= self._size:
            raise ListError('Out of range!')
        
        if index == self._size - 1:
            return self._tail.get_val()
        else:
            x_node = self._head
            for i in range(index):
               x_node = x_node.get_next()
            return x_node.get_val()
    
    def push_front(self, value):
        new_node = Node(value)
        x_node = self._head
        self._head = new_node
        self._head.set_next(x_node)
        self._size += 1
        if self._size == 1:
            self._tail = self._head
    
    def pop_front(self):
        if self._size == 0:
            return None
        x_node = self._head
        self._head = self._head.get_next()
        self._size -= 1 
        return x_node.get_val()
    
    def push_back(self, value):
        new_node = Node(value)
        if self._size != 0:
            x_node = self._tail
            self._tail = new_node
            x_node.set_next(self._tail)
        elif self._size == 0:
            self._head = self._tail = new_node
        self._size += 1

    def pop_back(self):
        x_node = self._head
        y_node = self._tail
        if self._size == 1:
            self._size -= 1
            return x_node.get_val()
        elif self._size == 0:
            return None
        for i in range(self._size-2): #获取倒数第2的Node
            x_node = x_node.get_next()
        self._tail = x_node
        self._tail.set_next(None)
        self._size -= 1
        return y_node.get_val()      
    
    def front(self):
        if self._size == 0: return None
        else: return self._head.get_val()
    
    def back(self):
        if self._size == 0: return None
        else: return self._tail.get_val()
    
    def insert(self, index, value):
        if index > self._size:
            raise ListError('Out of range!')
        elif index < 0:
            index = self._size - index
        elif index < -self._size:
            raise ListError('Out of range!')

        if index == 0:
            self.push_front(value)
        elif index == self._size:
            self.push_back(value)
        else:
            new_node = Node(value)
            x_node = self._head
            y_node = None

            for i in range(index-1):
                x_node = x_node.get_next()
            
            y_node = x_node.get_next()
            new_node.set_next(y_node)
            x_node.set_next(new_node)
            self._size += 1
    
    def erase(self, index):
        if index >= self._size:
            raise ListError("out of range!")
        if self._size == 1:
            x_node = self._head
            if index == 0:
                self._head = self._tail = None
        else:
            x_node = self._head
            y_node = None
            for i in range(index-1):
                x_node = x_node.get_next()
            y_node = x_node.get_next().get_next()
            x_node.set_next(y_node)
        self._size -= 1
    
    def value_n_from_end(self, n):
        if -n >= self._size:
            raise ListError("Out of range!")
        return self.value_at(n)
    
    def reverse(self):
        if self._size <= 1:
            return
        elif self._size == 2:
            self._head, self._tail = self._tail, self._head
            self._head.set_next(self._tail)
            self._tail.set_next(None)
        else:
            x_node = self._head
            y_node = x_node.get_next()
            z_node = y_node.get_next()
            x_node.set_next(None)

            for i in range(self._size-1):
                # print("round{}".format(i), x_node.get_val(), y_node.get_val(), z_node.get_val())
                y_node.set_next(x_node)
                x_node = y_node
                y_node = z_node
                if z_node.get_next() is not None:
                    z_node = z_node.get_next()
            self._head, self._tail = self._tail, self._head
    
    def remove_value(self, value):
        x_node = self._head
        for i in range(self._size):
            if value == x_node.get_val():
                self.erase(i)
            x_node = x_node.get_next()
                