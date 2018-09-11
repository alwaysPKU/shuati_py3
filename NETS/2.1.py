import sys

if __name__ == '__main__':
    s=sys.stdin.readline().rstrip()
    s=list(s)
    leth = len(s)
    print(s)
    for i in range(leth):
        if i+1<=leth-2 and s[i]==s[i+1]:
            s[0:i+1]=s[i:-1:-1]
            print(s)
            s[i+1:leth]=s[leth-1:i:-1]
            print(s)
    print(s)