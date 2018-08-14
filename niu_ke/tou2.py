if __name__ == '__main__':
    line = input()
    while line:
        m, n = [int(s) for s in line.split(' ')]
        dic = {}
        for _ in range(m):
            row = input()
            temp = dic
            for c in row:
                if c not in temp:
                    temp[c] = {}
                temp = temp[c]
            temp[-1] = None
        input()
        for _ in range(n):
            row = input()
            # print('num:',row)
            if row[0] not in dic:
                print(-1)
                continue
            temp = dic[row[0]]
            if -1 in temp:
                print(1)
                continue
            for c in row[1:]:
                if c not in temp:
                    print(-1)
                    break
                temp = temp[c]
                if -1 in temp:
                    print(1)
                    break
            print(-1)
        input()
        line = input()
        if line:
            print()


