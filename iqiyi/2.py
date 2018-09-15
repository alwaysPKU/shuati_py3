import sys


if __name__ == '__main__':
    num=int(sys.stdin.readline())
    ary=[]
    for i in range(num):
        tmp=list(map(int, sys.stdin.readline().rstrip().split()))
        tmp.sort()
        ary.append(tmp)
    ary.sort(key=lambda x:x[1])
    # print(ary)
    res=1
    mark=0
    for i in range(1,num):
        if ary[i][0]>=ary[mark][1]:
            res+=1
            mark=i
    print(res)
