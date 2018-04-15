import sys


def br(n1, n1_array, n2, n2_array, mark, m, res, tmp):
    if sum(tmp)==m:
        res+=1
    else:


if __name__ == '__main__':
    line = list(map(int, sys.stdin.readline().split(' ')))
    n1 = line[0]
    n2 = line[1]
    m = line[2]
    n1_array = list(map(int, sys.stdin.readline().split(' ')))
    n2_array = list(map(int, sys.stdin.readline().split(' ')))
    res = 0
    mark = [0]*n2
    tmp = []
    br(n1, n1_array, n2, n2_array, mark, m, res, tmp)
    print(res)


