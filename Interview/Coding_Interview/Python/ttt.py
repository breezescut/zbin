
import sys

def func(lt):
    h1, h2 = 0, 0
    
    for i in range(len(lt)):
        if h1 <= h2:
            # h1 += lt.pop()
            a = lt.pop()
            print('h1:', h1, 'h2:', h2, 'a:', a)
            h1 += a
            print('h1:', h1)
        else:
            # h2 += lt.pop()
            a = lt.pop()
            print('h1:', h1, 'h2:', h2, 'a:', a)
            h2 += a
            print('h2:', h2)
        print('')
    return max(h1,h2)
    
# n = sys.stdin.readline().strip()
# line = sys.stdin.readline().strip()
# lines = line.split()
# lt = [int(x) for x in lines]
# lt = [3072,3072,7168,3072,1024]
lt = [1411072,2110464,1388544,2362368,1103872,59392,133120,1184768,1500160,1332224]
lt.sort()
# lt.reverse()
print(lt)
print(func(lt))