import pudb; pu.db
 
def findinspt(x, xnew):
    n = len(x)
    lo = 0
    hi = n-1
    while True:
        mid = (lo + hi) / 2
        if xnew > x[mid]:
            lo = mid + 1
        else:
            hi = mid
        if xnew == x[mid]:
            return mid
 
if __name__ == "__main__":
    y = [5,12,13]
    print(findinspt(y,3))
    print(findinspt(y,8))
    print(findinspt(y,12))
    print(findinspt(y,30))
