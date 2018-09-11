if __name__ == '__main__':
    num=int(input())
    # print(num)
    graph=[]
    tmp=[]
    M=0
    for _ in range(num-1):
        ary=list(map(int, input().split()))
        M=max(max(ary),M)
        tmp.append(ary)
    tmp.sort()
    for _ in range(M):
        graph.append([])
    for pair in tmp:
        graph[pair[0]-1].append(pair[1]-1)
        graph[pair[1]-1].append(pair[0]-1)
    print(graph)
    