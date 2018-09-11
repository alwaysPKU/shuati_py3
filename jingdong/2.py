import sys


def judge(g,n):
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            elif not g[i][j]:
                for d in range(n):
                    if g[i][d] and not g[j][d]:
                        return 'No'
    return 'Yes'


if __name__ == '__main__':
    num=int(sys.stdin.readline().rstrip())
    for _ in range(num):
        node, edge = list(map(int, sys.stdin.readline().rstrip().split()))
        graph = [[0 for _ in range(node)] for _ in range(node)]
        for tmp in range(edge):
            i, j = list(map(int, sys.stdin.readline().rstrip().split()))
            graph[i-1][j-1] = 1
            graph[j-1][i-1] = 1
        res=judge(graph,node)
        print(res)