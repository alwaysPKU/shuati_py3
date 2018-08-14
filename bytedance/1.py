#coding=utf-8
import sys
'''
测试数据
10,10
0,0,1,1,1,0,1,0,0,0
0,0,0,1,1,0,1,0,0,0
1,0,1,1,1,0,1,0,0,0
0,0,0,0,0,0,0,0,0,0
0,0,1,1,1,0,1,0,0,0
0,0,1,1,1,0,1,0,0,0
0,0,0,0,0,0,0,0,0,0
0,0,1,1,1,0,1,0,0,0
0,0,1,1,1,0,1,0,0,0
0,0,1,1,1,0,1,0,0,0
'''


def judge(chairs,r,c,m,n):
    if r>m-1 or r<0 or c>n-1 or c<0 or (not chairs[r][c]):
        return
    else:
        global nums
        nums+=1
        chairs[r][c]=0
    judge(chairs, r, c+1, m, n)
    judge(chairs, r + 1, c+1, m, n)
    judge(chairs, r + 1, c, m, n)
    judge(chairs, r + 1, c-1, m, n)
    judge(chairs, r, c-1, m, n)
    judge(chairs, r - 1, c-1, m, n)
    judge(chairs, r - 1, c, m, n)
    judge(chairs, r - 1, c+1, m, n)


if __name__ == '__main__':
    line=sys.stdin.readline().strip().split(',')
    m=int(line[0])
    n=int(line[1])
    chairs=[]
    for i in range(m):
        line=list(map(int, sys.stdin.readline().strip().split(',')))
        chairs.append(line)
    groups=0
    biggest=0
    nums=0
    for row in range(m):
        for col in range(n):
            if chairs[row][col]:
                groups+=1
                judge(chairs,row,col,m,n)
                if biggest < nums:
                    biggest = nums
                nums=0
    print(groups)
    print(biggest)


