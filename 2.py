import sys


class Solution:
    def find_max_len(self, row, col, arr):
        all_list = []
        cur_add_list = []
        for ii in range(row):
            for jj in range(col):
                if arr[ii][jj] != 0:
                    if [ii, jj] in cur_add_list:
                        continue
                    else:
                        cur_add_list.extend([ii, jj])
                        out_list = [[ii, jj]]
                        search_list = [[ii, jj]]
                        while search_list:
                            cur_search = []
                            for file in search_list:
                                for direction in delta:
                                    pos = [file[0] + direction[0], file[1] + direction[1]]
                                    if row - 1 < pos[0] or pos[0] < 0 or col -1 < pos[1] or pos[1] < 0:
                                        continue
                                    elif pos in out_list:
                                        continue
                                    else:
                                        if arr[pos[0]][pos[1]] != 0:
                                            cur_search.append(pos)
                                            out_list.append(pos)
                            search_list = cur_search
                        all_list.append(out_list)
                        cur_add_list.extend(out_list)

        sum_list = []
        for file in all_list:
            sum_ = 0
            for num_ in file:
                sum_ += arr[num_[0]][num_[1]]
            sum_list.append(sum_)
        return [len(sum_list), max(sum_list)]


if __name__ == '__main__':
    delta = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    line=sys.stdin.readline().strip().split(',')
    m=int(line[0])
    n=int(line[1])
    chairs=[]
    for i in range(m):
        line=list(map(int, sys.stdin.readline().strip().split(',')))
        chairs.append(line)

    S = Solution()
    res = S.find_max_len(m, n, chairs)
    print(','.join(map(str,res)))
