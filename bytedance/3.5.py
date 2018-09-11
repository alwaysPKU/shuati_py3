import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip('\n'))
    m = int(sys.stdin.readline().rstrip('\n'))
    # ary= list(map(int,sys.stdin.readline().rstrip('\n').split()))
    ary=sys.stdin.readline().rstrip('\n')
    fensi={}
    for _ in range(m):
        l=_*4
        r=_*4+2
        if ary[r] in fensi:
            fensi[ary[r]].add(ary[l])
        else:
            fensi[ary[r]]=set(ary[l])
    # print(fensi)
    res=0
    for k,v in fensi.items():
        tmp_z_fen=len(v)
        for f in v:
            if k in fensi[f]:
                tmp_z_fen+=len(fensi[f])-1
            else:
                tmp_z_fen+=len(fensi[f])
        if tmp_z_fen==n-1:
            res+=1
    print(res)

