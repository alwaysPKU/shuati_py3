import sys

def tmp(a, b):
    a = a % b
    dic = {}
    pt = 0
    while True:
        dic[a] = pt
        pt += 1
        a *= 10
        a %= b
        if a == 0:
            return pt, 0
        if a in dic:
            return pt - 1, pt - dic[a]

if __name__ == "__main__":
    m, n = list(map(float,sys.stdin.readline().strip().split()))
    x, y = tmp(m ,n)
    print (x, y)