import sys


def judge(r,c,word,array):
    length=len(word)
    count=0
    for i,w in enumerate(word):
        if r+length>len(array):
            break
        elif array[r+i][c]==w and i+1==length:
            count+=1
        elif array[r+i][c]==w:
            continue
        else:
            break
    for i,w in enumerate(word):
        if c+length>len(array[0]):
            break
        elif array[r][c+i]==w and i+1==length:
            count+=1
        elif array[r][c+i]==w:
            continue
        else:
            break
    for i,w in enumerate(word):
        if c+length>len(array[0]) or r+length>len(array):
            break
        elif array[r+i][c+i]==w and i+1==length:
            count+=1
        elif array[r+i][c+i]==w:
            continue
        else:
            break
    return count

if __name__ == '__main__':
    num = int(sys.stdin.readline())
    for i in range(num):
        line1=list(map(int,sys.stdin.readline().rstrip().split(' ')))
        rows=line1[0]
        columns=line1[1]
        array=[]
        for r in range(rows):
            array.append(sys.stdin.readline().rstrip())
        word=sys.stdin.readline().rstrip()
        res=0
        for i in range(rows):
            for j in range(columns):
                num=judge(i,j,word,array)
                res+=num
        print(res)