# coding=utf-8
import sys

class pn:
    def __init__(self):
        self.childs = {}

    def add(self, string):
        if string:
            c = string[0]
            if c not in self.childs:
                self.childs[c] = pn()

            self.childs[c].add(string[1:])

def result(ps, k):
    for i in range(k, b):
        ps += ary[i][0]
    return ps

def get_str(pre_str, k, pre_node):
    if k == b:
        if pre_str not in ori:
            return pre_str
        else:
            return False
    temp_arr = ary[k]
    for s in temp_arr:
        if s not in pre_node.childs:
            return result(pre_str+s, k+1)
        else:
            tmp = get_str(pre_str+s, k+1, pre_node.childs[s])
            if tmp is not False:
                return tmp


if __name__ == '__main__':
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    ary = [['' for j in range(a)] for i in range(b)]
    ori = set()
    root = pn()

    for i in range(a):
        ss = sys.stdin.readline().strip()
        ori.add(ss)
        root.add(ss)
        for j, s in enumerate(ss):
            ary[j][i] = s
    for i in range(b):
        ary[i] = sorted(ary[i])
    print(get_str('', 0, root))
