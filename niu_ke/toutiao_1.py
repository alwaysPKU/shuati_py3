import sys
N = int(sys.stdin.readline())


def find_t(n, array):
    t=-1
    for i in range(n-1):
        new = array[i+1]-array[i]
        if t == -1:
            t = new
        else:
            for j in range(i+1):
                if array[j]+t>=array[i+1] or array[j]+t in array:
                    continue
                else:
                    t += new
    return t

res = []
for i in range(N):
    line = list(map(int, sys.stdin.readline().strip().split(' ')))
    n = line[0]
    array = line[1:]
    res.append(find_t(n, array))

for i in res:
    print(i)
