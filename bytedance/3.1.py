import sys


if __name__ == '__main__':
    line = sys.stdin.readline().rstrip('\n')
    mark=set()
    res=0
    tmp=0
    leth=len(line)
    for ind,i in enumerate(line):
        if i not in mark:
            mark.add(i)
            tmp+=1
        else:
            res = res if res>tmp else tmp
            mark.clear()
            mark.add(i)
            tmp=1
        if ind==leth-1:
            res = res if res > tmp else tmp
    print(res)
