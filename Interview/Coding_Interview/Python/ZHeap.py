#! /usr/bin/env python

import math

class ZHeap():
    def __init__(self):
        self.size = 0
        self.heap = []
    
    @staticmethod
    def less(x, y):
        if x < y:
            return True
        else:
            return False
    
    
    def exch(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
        
    
    @staticmethod
    def parent(idx):
        return math.ceil(idx/2) - 1

    @staticmethod
    def left_child(idx):
        return idx * 2 + 1
    
    @staticmethod
    def right_child(idx):
        return idx*2 + 2

    def sift_up(self, idx):
        while idx > 0 and self.less(self.heap[self.parent(idx)], self.heap[idx]):
            self.exch(self.parent(idx), idx)
            idx = self.parent(idx)
    
    # def sift_down(self, idx):
    #     while idx <= int(self.size/2) - 1 and \
    #         self.left_child(idx) < self.size and \
    #         self.right_child(idx) < self.size:
    #         if self.less(self.heap[self.left_child(idx)], self.heap[self.right_child(idx)]):
    #             if self.less(self.heap[idx], self.heap[self.right_child(idx)]):
    #                 self.exch(idx, self.right_child(idx))
    #                 idx = self.right_child(idx)
    #             else:
    #                 break
    #         else:
    #             if self.less(self.heap[idx], self.heap[self.left_child(idx)]):
    #                 self.exch(idx, self.left_child(idx))
    #                 idx = self.left_child(idx)
    #             else:
    #                 break

    def sift_down(self, idx):
        while idx*2+1 <= self.size-1:
            j = idx*2 + 1
            if j < self.size-1 and self.less(self.heap[j], self.heap[j+1]):
                j += 1
            if self.less(self.heap[idx], self.heap[j]) != True:
                break
            self.exch(idx, j)
            idx = j

    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        self.sift_up(self.size - 1)
        
    def extract_max(self):
        self.exch(0, self.size-1)
        max_item = self.heap.pop()
        self.size -= 1
        self.sift_down(0)
        return max_item
    
    def get_max(self):
        return self.heap[0]
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def remove(self, idx):
        self.heap[idx] = float('inf')
        sift_up(idx)
    
    def __str__(self):
        return ' '.join(str(self.heap))
    
    @staticmethod
    def heapify(lt):
        zheap = ZHeap()
        zheap.heap = lt[:]
        zheap.size = len(lt)
        for idx in range(int(zheap.size/2)-1, -1, -1):
            zheap.sift_down(idx)
        return zheap

    @staticmethod
    def heap_sort(lt):
        zheap = ZHeap.heapify(lt)
        lt = []
        for i in range(zheap.size):
            lt.append(zheap.extract_max())
        return lt


    

        
             



