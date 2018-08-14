import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    for _ in range(N):
        line = sys.stdin.readline().strip()
        arr = [int(s) for s in line.split(' ')]
        n, m = arr[0], arr[1]
        arr = arr[2:]
        lst = [i for i in range(n)]
        start = 0
        index = 0
        while len(lst) != 1:
            step = arr[index]
            temp = (start + step - 1) % len(lst)
            lst[temp:-1] = lst[temp + 1:]
            lst = lst[:-1]
            start = (temp + 1) % len(lst)
            index = (index + 1) % m
        print(lst[0])
