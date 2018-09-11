import sys

def judge(step, res):
    if (step, res) in dp:
        return dp[(step, res)]
    if step <= 0 or step < res - 1:
        return 0
    if res == 0:
        if 0 < int(line[:step]) < 255:
            return 1
        else:
            return 0
    total = 0
    for k in range(step-1, 0, -1):
        if k == step - 1:
            total += judge(k, res - 1)
        elif line[k] != '0' and 0 < int(line[k:step]) <= 255:
            total += judge(k, res-1)
        elif int(line[k:step]) > 255:
            break
    dp[(step, res)] = total
    return dp[(step, res)]


if __name__ == '__main__':
    line = sys.stdin.readline().rstrip('\n')
    dp = {}
    res = judge(len(line), 3)
    print(res)