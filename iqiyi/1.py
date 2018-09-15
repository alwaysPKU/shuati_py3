import sys


if __name__ == '__main__':
    n,m,p = list(map(int, sys.stdin.readline().rstrip().split()))
    ai=list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(m):
        line=sys.stdin.readline().rstrip().split()
        index=int(line[1])-1
        if line[0]=='A':
            ai[index]+=1
        else:
            ai[index] -= 1
    target=ai[p-1]
    res=0
    # print(ai)
    for t in ai:
        if t>target:
            res+=1
    print(res+1)
