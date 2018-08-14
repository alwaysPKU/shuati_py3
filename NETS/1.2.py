#coding=utf-8
import sys

if __name__ == '__main__':
    nums=int(sys.stdin.readline().strip())
    shenfen={}
    for i in range(nums):
        line=sys.stdin.readline().strip().split()
        shenfen[line[1]]=int(line[0])
    nums_status=int(sys.stdin.readline().strip())
    ids=[]
    status=[]
    status_res={}
    for i in range(nums_status):
        line = sys.stdin.readline().strip().split()
        ids.append(line[0])
        status.append(line[1])
        status_res[line[0]]='0'
        # print(status_res)
    ids.reverse()
    status.reverse()
    for index,i in enumerate(ids):
        for j in range(index+1,len(ids)):
            if ids[index]==ids[j]:
                ids[j]=''
    for index,i in enumerate(ids):
        if i:
            status_res[i]=status[index]
    zaixian=[]
    lixian=[]
    for k,v in status_res.items():
        if v=='1':
            zaixian.append(k)
        else:
            lixian.append(k)
    zaixian.sort()
    lixian.sort()
    zaixian.sort(key=lambda x:shenfen[x],reverse=True)
    lixian.sort(key=lambda x: shenfen[x],reverse=True)
    for i in zaixian:
        print(i)
    for i in lixian:
        print(i)

