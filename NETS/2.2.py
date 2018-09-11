import sys


def change(i,j):
    global matrix
    if i>=0 and i<=n-1 and j>=0 and j<=m-1:
        if matrix[i][j]:
            matrix[i][j]=0
        else:
            matrix[i][j]=1


def count(h,l):
    c=0
    for i in range(h):
        for j in range(l):
            change(i,j)
            change(i-1,j-1)
            change(i-1,j)
            change(i-1,j+1)
            change(i, j-1)
            change(i+1,j+1)
            change(i+1,j)
            change(i+1,j-1)
            change(i,j+1)
    for i in range(h):
        for j in range(l):
            if matrix[i][j]:
                c+=1
    return c


if __name__ == '__main__':
    eg=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(eg):
        n,m=list(map(int, sys.stdin.readline().rstrip('\n').split()))
        global matrix
        matrix=[[0 for _ in range(m)] for _ in range(n)]
        res=count(n,m)
        print(res)
