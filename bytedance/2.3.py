import sys

def judge(l,r):
    if l==r:
        return 'Yeah'
    if len(l)!=len(r):
        return 'Sad'
    length=len(l)
    pianzhi=range(length)
    for p in pianzhi:
        count=0
        for i in range(length):
            if l[(p+i)%length] != r[i]:
                break
            else:
                count+=1
            if count==length:
                return 'Yeah'
    for p in pianzhi:
        count=0
        for i in range(length):
            if l[(p+i)%length] != r[length-i-1]:
                break
            else:
                count+=1
            if count==length:
                return 'Yeah'
    return 'Sad'
if __name__ == '__main__':
    num=int(sys.stdin.readline().strip())
    for i in range(num):
        sys.stdin.readline()
        s1=sys.stdin.readline().strip()
        s2=sys.stdin.readline().strip()
        res=judge(s1, s2)
        print(res)

