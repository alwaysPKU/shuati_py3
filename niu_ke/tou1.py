import sys

ans = 0
left = 0
# right = 0
mark = True
for line in sys.stdin:
    num = 0
    line = line.strip('\n')
    length = len(line)
    for i in range(length):
        if line[i] == '/' and i+1<length and line[i+1] == '/' and mark and i+1 != length-1:
            ans += 1
        if line[i] == '/' and i+1<length and line[i+1] == '*' and left==0 and mark:
            left = 1
        if line[i] == '*' and i+1<length and line[i+1] == '/' and left==1 and mark:
            ans += 1
            left = 0
        if line[i] == '"' and num == 0 and left == 0:
            mark = False
            num = 1
        if line[i] == '"' and num == 1:
            mark = True
            num = 0
print(ans)

