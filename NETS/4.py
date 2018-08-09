import sys


if __name__ == '__main__':
    line1=list(map(int, input().rstrip().split()))
    jobs=line1[0]
    friends=line1[1]
    di=[]
    pi=[]
    for i in range(jobs):
        ary=list(map(int, input().rstrip().split()))
        di.append(ary[0])
        pi.append(ary[1])
    line2=input().rstrip().split()
    nengli=list(map(int, line2))
    di_new=[]
    pi_new=[]
    for d,p in sorted(zip(di, pi), key=lambda x: x[0]):
        di_new.append(d)
        pi_new.append(p)
    for i in nengli:
        res=0
        for index,j in enumerate(di_new):
            if i >= j:
                res=pi_new[index]
                continue
            else:
                break
        print(res)


