#! /usr/bin/env python

import unittest
from ZList import Node, Zlist, ListError

class TestNode(unittest.TestCase):
    def setUp(self):
        pass
    def test_node(self):
        x_node = Node()
        self.assertIsInstance(x_node.get_val(), object)
        x_node.set_next(Node(1))
        y_node = x_node.get_next()
        self.assertEqual(y_node.get_val(), 1)

class TestZList(unittest.TestCase):
    def test_init(self):
        x = [1,2,3]
        x[0] = [1,2,2,3,3223,4,32,5,43,543,5,4,645,64,'','32432','324saf']
        x[1] = []
        x[2] = [None, None, 'xxx', 1,2, 3,34]

        for xx in x:
            lt = Zlist(xx)
            x_node = None
            for i in range(lt.get_size()):
                if i == 0: x_node = lt._head
                else:x_node = x_node.get_next()
                
                if xx[i] is None: self.assertIsInstance(x_node.get_val(), object)
                else: self.assertEqual(xx[i], x_node.get_val())
    
    def test_value_at(self):
        xx = [1,2,2,3,3223,4,32,5,43,543,5,4,645,64,'','32432','324saf']
        lt1 = Zlist(xx)
        lt2 = Zlist()

        for i in range(len(xx)):
            # print(lt1.value_at(i), xx[i])
            self.assertEqual(lt1.value_at(i), xx[i])
        
        with self.assertRaises(ListError) as ex:
            lt1.value_at(len(xx))
        
        for i in range(3):
            with self.assertRaises(ListError) as ex:
                lt2.value_at(i)
        
    def test_push_front(self):
        lt1 = Zlist()
        xx = [1,2,2,3,3223,4,32,5,43,543,5,4,645,64,'','32432','324saf']
        for i in range(len(xx)):
            lt1.push_front(xx[i])
            self.assertEqual(lt1.value_at(0), xx[i])
            self.assertEqual(lt1.get_size(), i+1)

    def test_pop_front(self):
        xx = [1,2,2,3,3223,4,32,5,43,543,5,4,645,64,'','32432','324saf']
        lt = Zlist(xx)
        for i in range(len(xx)):
            self.assertEqual(lt.pop_front(), xx[i])
            self.assertEqual(lt.get_size(), len(xx)-i-1)
        self.assertEqual(lt.pop_front(), None)
    
    def test_push_bask(self):
        xx = [1,2,2,3,3223,4,32,5,43,543,5,4,645,64,'','32432','324saf']
        lt1 = Zlist()
        for i in range(len(xx)):
            lt1.push_back(xx[i])
            self.assertEqual(xx[i], lt1.value_at(i))
            self.assertEqual(lt1.get_size(), i+1)

    def test_pop_back(self):
        xx = [1,2,2,3,3223,4,32,5,43,543,5,4,645,64,'','32432','324saf']
        lt = Zlist(xx)
        len_xx = len(xx)
        for i in range(len_xx):
            # print(lt.pop_back(), xx[len_xx-i-1])
            lt_val = lt.pop_back()
            # print("test:", lt_val, xx[len_xx-i-1])
            self.assertEqual(lt_val, xx[len_xx-i-1])
            self.assertEqual(lt.get_size(), len(xx)-i-1)
        self.assertEqual(lt.pop_back(), None)

    def test_front(self):
       pass
    
    def test_back(self):
        pass
    
    def test_insert(self):
        xx = [1,2,2,3,3223,4,32,5,43,543,5,4,645,64,'','32432','324saf']
        lt = Zlist(xx)

        with self.assertRaises(ListError) as ex:
            lt.insert(lt.get_size()+1, 111)
        
        xx2 = xx[:]
        for i in range(10):
            xx2.insert(i, i)
            lt.insert(i, i)
            self.assertEqual(xx2[i], lt.value_at(i))
        
        lt2 = Zlist()
        # print(lt2.get_size())
        lt2.insert(0, 1)
        # print(lt2.get_size())
        self.assertEqual(lt2.front(), 1)
        lt2.pop_back()
        # print(lt2.get_size())
        with self.assertRaises(ListError) as ex:
            lt2.insert(1, 1)
        pass
    
    def test_erase(self):
        pass
    
    def test_value_n_from_end(self):
        pass
    
    def test_reverse(self):
        xx = [1,2,2,3,3223,4,32,5,43,543,5,4,645,64,'','32432','324saf']
        lt = Zlist(xx)
        lt.reverse()
        xx.reverse()
        for i in range(len(xx)):
            # print(lt.value_at(i), xx[i])
            self.assertEqual(lt.value_at(i), xx[i])

    def test_remove_value(self):
        pass

if __name__ == '__main__':
    unittest.main()