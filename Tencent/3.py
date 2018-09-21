import sys


if __name__ == '__main__':
    a,b,c = list(map(int, sys.stdin.readline().rstrip().split()))
    res=0
    for i in range(1,a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                if i <= j <= k:
                    if i+j > k:
                        res+=1
                    else:
                        break
                
    print(res%1000000007)