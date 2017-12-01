
import unittest

class TestArray(unittest.TestCase):

    def test_2_1_1(self):
        def solution1(marr):
            j = 0
            for i in range(1, len(marr)):
                if marr[i] != marr[j]:
                    j += 1
                    marr[j] = marr[i]
            for x in range(j+1, len(marr)):
                marr.pop()
            return j+1, marr

        # 这个是为unsorted array准备的解法
        def solution2(marr):
            j = 0

            for i in range(1, len(marr)):
                for x in range(0, j+1):
                    if marr[i] == marr[x]:
                        break
                else:
                    j += 1
                    marr[j] = marr[i]
            for x in range(j+1, len(marr)):
                marr.pop()
            return len(marr), marr
        
        marr1 = [1,1,1,1,2,2,2,2,3,4,4,5,5]
        len_marr1, marr1 = solution1(marr1)
        print('len:{}, marr1:{}'.format(len_marr1, marr1))

        marr2 = [1,1,2,2,3,4,3,4,2,5,5,5,5,5,5,4,6,'122']
        len_marr2, marr2 = solution2(marr2)
        print('len:{}, marr2:{}'.format(len_marr2, marr2))

    def test_2_1_2(self):
        def solution1():
            '''
            直接比较之前出现过的元素, 有相同元素且
            '''

if __name__ == '__main__':
    unittest.main()