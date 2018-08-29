#coding=utf-8
import sys

import sys


def judge(a,b):
    for i in range(b):
        for j in range(b):
            x = list(set(a[i] + a[j]))
            y = len(a[j]) + len(a[i])
            if i == j or a[i] == 0 or a[j] == 0:
                break
            elif len(x) < y:
                a[i] = x
                a[j] = [0]
    # print([i for i in a if i != [0]])
    return len([i for i in a if i !=[0]])

if __name__ == '__main__':
    num=int(sys.stdin.readline().strip())
    labels=[]
    for i in range(1,num+1):
        # print(i)
        ary=list(map(int, sys.stdin.readline().rstrip().split()))
        ary.remove(0)
        ary.append(i)
        labels.append(ary)
    # print(labels)
    res=judge(labels, num)
    print(res)

