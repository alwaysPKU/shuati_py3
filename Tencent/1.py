import sys


def count(s_a, s_b):
    l1=len(s_a)
    l2=len(s_b)
    cou=0
    if l1 > l2:
        return cou
    for i in range(l2-l1+1):
        if s_b[i:i+l1] == s_a:
            cou+=1
    return cou
if __name__ == '__main__':
    k = int(sys.stdin.readline().rstrip())
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()
    set_a=set()
    if k > len(b):
        print(0)
    else:
        for i in range(len(a)-k+1):
            set_a.add(a[i:k+i])
        res=0
        for sub in set_a:
            tmp=count(sub,b)
            res+=tmp
        print(res)
