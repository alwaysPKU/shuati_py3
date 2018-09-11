import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    graph = [[0 for j in range(n)] for i in range(n)]
    for i in range(m):
        a, b = nums[2*i], nums[2*i + 1]

        graph[a-1][b-1] = 1
    for step in range(n):

        for i in range(n):
            for j in range(n):

                if i != j and graph[i][step] == 1 and graph[step][j] == 1:
                    graph[i][j] = 1
    total = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if graph[j][i] == 1:
                cnt += 1
        if cnt == n-1:
            total += 1
    print(total)