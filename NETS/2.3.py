import sys


if __name__ == '__main__':
    eg=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(eg):
        n,m=list(map(int, sys.stdin.readline().rstrip('\n').split()))
        if n==m==1:
            print(1)
        elif m==1:
            print(n-2)
        elif n==1:
            print(m-2)
        else:
            res=(n-2)*(m-2)
            # res = 0 if res==1 else res
            print(res)
