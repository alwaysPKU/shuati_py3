#coding=utf-8
import sys


def judge(chairs,r,c,m,n):
    if r>m-1 or r<0 or c>n-1 or c<0 or (not chairs[r][c]):
        return
    else:
        # global nums
        # nums+=1
        chairs[r][c]=0
    judge(chairs, r, c+1, m, n)
    # judge(chairs, r + 1, c+1, m, n)
    judge(chairs, r + 1, c, m, n)
    # judge(chairs, r + 1, c-1, m, n)
    judge(chairs, r, c-1, m, n)
    # judge(chairs, r - 1, c-1, m, n)
    judge(chairs, r - 1, c, m, n)
    # judge(chairs, r - 1, c+1, m, n)


if __name__ == '__main__':
    num=int(sys.stdin.readline().rstrip('\n'))
    # line=sys.stdin.readline().strip().split(',')
    # m=int(line[0])
    # n=int(line[1])
    chairs=[]
    for _ in range(num):
        chairs.append(list(map(int, sys.stdin.readline().strip().split())))
    m=num
    n=len(chairs[0])
    groups=0
    # biggest=0
    # nums=0
    for row in range(m):
        for col in range(n):
            if chairs[row][col]:
                groups+=1
                judge(chairs,row,col,m,n)
    print(groups)



