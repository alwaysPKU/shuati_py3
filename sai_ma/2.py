def find(n, nums):
    slower=0-n
    p = 0
    m = 0
    for i in range(leth):
        if nums[i]==0:
            p=i-slower
            slower=i
        m=max(m, i-slower+p)
    return m
if __name__ == '__main__':
    ary=input().split()
    leth,chance=list(map(int, ary))
    ary=list(map(int,input().split()))
    res=find(chance,ary)
    print(res)

