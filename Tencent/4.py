import sys

if __name__ == '__main__':
    num = int(sys.stdin.readline().rstrip())
    ary=[]
    for _ in range(num):
        ary.append(int(sys.stdin.readline().rstrip()))
    res=0
    sign=1
    size=len(ary)
    for i in range(size // 2):
        if sign:
            sign = 0
            for j in range(i, size - 1 - i):
                if ary[j] > ary[j + 1]:
                    res+=1
                    ary[j], ary[j + 1] = ary[j + 1], ary[j]
            for k in range(size - 2 - i, i, -1):
                if ary[k] < ary[k - 1]:
                    res+=1
                    ary[k], ary[k - 1] = ary[k - 1], ary[k]
                    sign = 1
        else:
            break
    print(res)
