import sys

def longest(arr):
    n = len(arr)
    m = [0] * n
    for x in range(n - 2, -1, -1):
        for y in range(n - 1, x, -1):
            if arr[x] <= arr[y] and m[x] <= m[y]:
                m[x] += 1
        max_value = max(m)
        result = []
        for i in range(n):
            if m[i] == max_value:
                result.append(arr[i])
                max_value -= 1
    # print(arr)
    # print(result)
    return len(result)

if __name__ == '__main__':
    ary=list(map(int, sys.stdin.readline().rstrip().split()))
    num=ary[1]
    res=[]
    ary_tmp=list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(num):
        res.extend(ary_tmp)
    print(longest(res))