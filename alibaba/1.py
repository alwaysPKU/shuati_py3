#coding=utf-8
import sys
import re
if __name__ == '__main__':
    line=sys.stdin.readline().rstrip('\n')
    entitys=line.split(';')
    entity_dic={}
    pattens=[]
    for i,en in enumerate(entitys):
        entity, p = en.split('_')
        pattens.append(p)
        entity_dic[entity]=pattens[i]
    query = sys.stdin.readline().rstrip('\n')
    query_list=[]
    for i in range(len(query)):
        query_list.append(query[i])
    mark=[]
    for entity, patten in entity_dic.items():
        for match in re.finditer(patten,query):
            s = match.start()
            e = match.end()
            tmp=[(s,e),entity]
            mark.append(tmp)
    mark.sort()
    leth=len(mark)
    num=[]
    name=[]
    for i in range(leth):
        if i+1<=leth-1 and mark[i+1][0][0]==mark[i][0][0]:
            continue
        else:
            num.append(mark[i][0])
            name.append(mark[i][1])
    res=''
    i=0
    print(num)
    left=0
    for i,n in zip(num,name):
        # print(i,n)
        for index in range(left,i[0]):
            res+=query_list[index]
            left=i[1]
        res+=' '
        for index in range(i[0], i[1]):
            res+=query_list[index]
        res = res + '/'+n+' '
    print(res)

