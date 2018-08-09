import sys

if __name__ == '__main__':
    num=int(sys.stdin.readline())
    num1=[]
    num_arry=[]
    for i in range(num):
        sys.stdin.readline()
        num_arry.append(sys.stdin.readline().rstrip())
    for l in num_arry:
        l=l.split(' ')
        l.reverse()
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i]==l[j]:
                    l[j]=''
        res=''
        for i in l:
            if i:
                res+=i+' '
        print(res)



