import sys, math


def cou(n):
    return math.sqrt(2*n+1/4)-1/2

if __name__ == '__main__':
    x, y = map(int,sys.stdin.readline().rstrip().split())
    res = cou(x+y)
    if int(res)!=res:
        print(-1)
    else:
        count=0
        res=int(res)
        for i in range(res,0,-1):
            # print('i-->',i,'x-->',x)
            if i < x:
                x-=i
                count+=1
            else:
                count+=1
                break
        print(count)


