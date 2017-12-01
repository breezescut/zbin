
import unittest
from ZHeap import ZHeap

class TestZHeap(unittest.TestCase):

    # def setUp(self):
    #     self.zheap = ZHeap()

    # def insert(self):
    #     for i in range(10):
    #         # print('Before insert:', zheap)
    #         self.zheap.insert(i)
    #         # print('After insert:', self.zheap)
    
    # def test_extract_max(self):
    #     zheap = self.zheap
    #     self.insert()
    #     # print(zheap)
    #     lt = []
    #     for i in range(zheap.size):
    #         lt.append(zheap.extract_max())
    #     print(lt)
    
    def test_heap_sort(self):
        lt = [1,24,5421,1123423,1,-1,2,2,2,2,4567,331,88]
        lt = ZHeap.heap_sort(lt)
        print(lt)

if __name__ == '__main__':
    unittest.main()