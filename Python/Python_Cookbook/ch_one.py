#! /usr/bin/env python

import unittest


class TestChOne(unittest.TestCase):

    def n_test_1_1(self):
        p = [1, 2, 3, 4, 5]
        a, b, c, _, _ = p  # 解系列的值数量要与列表的一致, 不想要的可以用 _ 代替
        print(a, b, c)

        a, b, c = range(1, 4)  # 生成器也是可以当系列进行解压
        print(a, b, c)

    def n_test_1_2(self):
       a = 'sagdhsagjfgsagfdsafdsh'
       b, *c, d, e = a  # 中间的 c 不会保持str , 而是会成为列表
       print(b, c, d, e)
       print(a)

       a = 'ab'
       b, *c, d = a
       print(b, c, d)

    def n_test_1_3(self):
        from collections import deque

        def search(context, pattern, history=5):
            prevLines = deque(maxlen=history)
            for line in context:
                line = line.strip('\n')
                if pattern in line:
                    prevLines.append(line)
                    yield line, prevLines

        with open(r'./somefile.txt') as f:
            for line, prevLines in search(f, 'python'):
                print("line:", line)
                print("prevLines:", prevLines)
                print('-' * 20)

    def n_test_1_4(self):
        # 1.4 查找最大或最小的N个元素
        import heapq

        nums = [1, 143, 4365, 56, 43, 23, 32, 432, 432, 4, 32, 43, 6, 456, 456]
        a = heapq.nlargest(3, nums)
        print(a)
        b = heapq.nsmallest(3, nums)
        print(b)

        portfolio = [
            {'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.75},
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'ACME', 'shares': 75, 'price': 115.65}
        ]

        expensive = heapq.nlargest(3, portfolio, key=lambda x: x['price'])
        cheap = heapq.nsmallest(3, portfolio, key=lambda x: x['price'])

        print(expensive)
        print(cheap)

    def n_test_1_5(self):
        #1.5 实现一个优先级队列
        import heapq

        class priorityQueue():
            def __init__(self):
                self.queue = []
                self.index = 0

            def push(self, item, priority):
                heapq.heappush(self.queue, (-priority, self.index, item))
                self.index += 1

            def pop(self):
                return "item{'%s'}" % (heapq.heappop(self.queue)[-1])
            
            def get_nums(self):
                return len(self.queue)
        
        queue = priorityQueue()
        queue.push('gary', 10)
        queue.push('kan', 9)
        queue.push('alex', 8)
        queue.push('mach', 7)
        queue.push('kelly', 7)

        for i in range(queue.get_nums()):
            print(queue.pop())
        
    def n_test_1_6(self):
        from collections import defaultdict

        d = defaultdict(list)
        d['a'].append(1)
        d['a'].append(2)
        d['b'].append(2)
        d['b'].append(3)

        print(d)
    
    def n_test_1_7(self):
        from collections import OrderedDict

        d = OrderedDict()
        d['foo'] = 1
        d['ss'] = 2
        d['xx'] = 3
        print([ x for x in d.keys()])

        import json
        x = json.dumps(d)
        print(x)

        e = {}
        e['foo'] = 2
        e['ss'] = 1
        e['xx'] = 3
        print([x for x in e.keys()])

    def n_test_1_8(self):
        def myzip(*iterables):
            iters = [iter(x) for x in iterables]
            terminal = object()
            while True:
                result = []
                for it in iters:
                    item = next(it, terminal)
                    if item is terminal:
                        return
                    result.append(item)
                yield tuple(result)
        prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }

        min_v = min(zip(prices.values(), prices.keys()))
        max_v = max(zip(prices.values(), prices.keys()))
        print(min_v, max_v)

        min_v = min(myzip(prices.values(), prices.keys()))
        max_v = max(myzip(prices.values(), prices.keys()))
        print(min_v, max_v)

        for i in myzip(prices.values(), prices.keys()):
            print(i)

    def n_test_1_9(self):
        a = {
            'x': 1,
            'y': 2,
            'z': 3
        }

        b = {
            'w': 10,
            'x': 11,
            'y': 2
        }

        common_keys = a.keys() & b.keys()
        notINB_keys = a.keys() - b.keys()
        #common_values = a.values() & b.values()
        common_items = a.items() & b.items()

        print(common_keys, notINB_keys , common_items)

    def n_test_1_10(self):
        def dedupe(items, key=None):
            seen = set()
            for i in items:
                val = i if key is None else key(i)
                if val not in seen:
                    yield i
                seen.add(val)
        
        a = [1, 5, 2, 1, 9, 1, 5, 10]
        print(list(dedupe(a)))

        a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
        print(list(dedupe(a, key = lambda d: (d['x'], d['y']))))

    def n_test_1_11(self):
         items = [0, 1, 2, 3, 4, 5, 6]

         a = slice(2, 4)

         self.assertEqual(items[2:4], items[a])

    def n_test_1_12(self):
        words = [
             'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
             'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
             'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
             'my', 'eyes', "you're", 'under'
        ]

        from collections import Counter
        words_count = Counter(words)

        most = words_count.most_common(3)
        print(most)

        morewords = ['why','are','you','not','looking','in','my','eyes']
        more_counter = Counter(morewords)
        
        new_counter = words_count + more_counter

        print(new_counter)

    def n_test_1_13(self):
        rows = [
            {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
            {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
            {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
            {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
        ]

        rows_by_fname = sorted(rows, key=lambda d: d['fname'])
        rows_by_uid = sorted(rows, key=lambda d: d['uid'])

        from operator import itemgetter
        rows_by_fname2 = sorted(rows, key = itemgetter('fname'))
        assertEqual(rows_by_fname, rows_by_fname2)

        rows_by_uid2 = sorted(rows, key = itemgetter('uid'))

        print(rows_by_fname)
        print(rows_by_uid)

        rows_by_lfname = sorted(rows, key=lambda d: (d['lname'], d['fname']))
        print(rows_by_lfname)
    
    def n_test_1_14(self):
        class User():
            def __init__(self, id):
                self.userid = id
            def __repr__(self):
                return "User{%s}" % self.userid
        
        users = []
        users.append(User(1))
        users.append(User(4))
        users.append(User(3))
        users.append(User(9))

        user_sorted1 = sorted(users, key=lambda i: i.userid)
        print(user_sorted1)
        
        from operator import attrgetter
        user_sorted2 = sorted(users, key=attrgetter('userid'))
        self.assertEqual(user_sorted1, user_sorted2)

        print(min(users, key=lambda u: u.userid))
        print(max(users, key=lambda u: u.userid))

    def n_test_1_15(self):
        rows = [
            {'address': '5412 N CLARK', 'date': '07/01/2012'},
            {'address': '5148 N CLARK', 'date': '07/04/2012'},
            {'address': '5800 E 58TH', 'date': '07/02/2012'},
            {'address': '2122 N CLARK', 'date': '07/03/2012'},
            {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
            {'address': '1060 W ADDISON', 'date': '07/02/2012'},
            {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
            {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
        ]

        # 使用 defauldict
        from collections import defaultdict
        rows_dict = defaultdict(list)
        for item in rows:
            rows_dict[item['date']].append(item)
        for date_key in sorted(rows_dict.keys()):
            print(date_key)
            for item in rows_dict[date_key]:
                print(" "*2, item)
        
        print('-'*20)
        # 使用 Groupby
        from itertools import groupby
        from operator import itemgetter
        rows.sort(key=itemgetter('date'))

        for key, items in groupby(rows, key=itemgetter('date')):
            print(key)
            for i in items:
                print(" " * 2, i)

    # 1.16 过滤序列元素
    def n_test_1_16(self):
        # 列表推导去除小于0元素
        mylist = [1, 4, -5, 10, -7, 2, 3, -1]
        for i in (n for n in mylist if n > 0):
            print(i)
        
        #clip_neg = [n if n > 0 else 0 for n in mylist]
        clip_neg = [n for n in mylist if n > 0 ]
        print(clip_neg)

        addresses = [
            '5412 N CLARK',
            '5148 N CLARK',
            '5800 E 58TH',
            '2122 N CLARK',
            '5645 N RAVENSWOOD',
            '1060 W ADDISON',
            '4801 N BROADWAY',
            '1039 W GRANVILLE',
        ]

        new_addresses = [n for n in addresses if 'CLARK' in n]
        print(new_addresses)

        L1 = ['Hello', 'World', 18, 'Apple', None]
        L2 = [n for n in L1 if isinstance(n, str)]
        print(L2)
        
        # 使用 filter 处理列表
        values = ['1', '2', '-3', '-', '4', 'N/A', '5'] 
        def is_int(val):
            try:
                x = int(val)
                return True
            except ValueError:
                return False
        new_values = list(filter(is_int, values))
        print(new_values)

    # 1.17 从字典中提取子集
    def n_test_1_17(self):
        prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }

        tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
        p1 = { key: value for key, value in prices.items() if key in tech_names and value>200 }
        print(p1)
    
    # 1.18 映射名称到序列元素
    def n_test_1_18(self):
        from collections import namedtuple

        Stocker = namedtuple('Stocker', ['name', 'share', 'price'])
        def compute_st(records):
            total = 0.0
            for rec in records:
                s = Stocker(*rec)
                total += s.share * s.price
            return total
        
        stock_info = [
            ['a', 10, 10.2],
            ['b', 20, 1324]
        ]
        x = compute_st(stock_info)
        print(x)

    # 1.19 转换并同时计算数据
    def test_1_19(self):
        import os
        files = os.listdir(r'E:\WorkHome\CodeHome\Python\Python_Cookbook')
        if any(name.endswith('.py') for name in files):
            print("found python files")
            print([name for name in files if name.endswith('.py')])
        else:
            print("no found any python files")
        
        s = ('ACME', 50, 123.45)
        print(','.join(str(i) for i in s))

        portfolio = [
            {'name': 'GOOG', 'shares': 50},
            {'name': 'YHOO', 'shares': 75},
            {'name': 'AOL', 'shares': 20},
            {'name': 'SCOX', 'shares': 65}
        ]

        min_shares = min(s['shares'] for s in portfolio)
        print(min_shares)
