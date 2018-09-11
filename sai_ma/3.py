import sys


def judge(step, res):
    if (step, res) in dp:
        return dp[(step, res)]
    if step < 0:
        return 0
    if nums[step] == 1:
        dp[(step, res)] = judge(step-1, res) + 1
    else:
        if res:
            dp[(step, res)] = judge(step-1, res-1) + 1

    return dp[(step, res)]


if __name__ == '__main__':
    N, K = list(map(int, sys.stdin.readline().rstrip().split()))
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    dp = {}
    for i in range(N):
        if nums[i] == 0:
            dp[(i, 0)] = 0
    print(max([judge(i, K) for i in range(N)]))


singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪
给我来一首周杰伦的七里香