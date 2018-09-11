import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    leth=len(nums)
    if leth==1:
        i2b = bin(nums[0]).split('b')[1]
        if i2b.startswith('0'):
            print(1)
        else:
            print(0)
    if leth==2:
        i2b_1 = bin(nums[0]).split('b')[1]
        i2b_2 = bin(nums[1]).split('b')[1]
        if i2b_1.startswith('110') and i2b_2.startswith('10'):
            print(1)
        else:
            print(0)
    if leth ==3:
        i2b_1 = bin(nums[0]).split('b')[1]
        i2b_2 = bin(nums[1]).split('b')[1]
        i2b_3 = bin(nums[1]).split('b')[1]
        if i2b_1.startswith('1110') and i2b_2.startswith('10') and i2b_3.startswith('10'):
            print(1)
        else:
            print(0)
    if leth ==4:
        i2b_1 = bin(nums[0]).split('b')[1]
        i2b_2 = bin(nums[1]).split('b')[1]
        i2b_3 = bin(nums[1]).split('b')[1]
        i2b_4 = bin(nums[1]).split('b')[1]
        if i2b_1.startswith('1110') and i2b_2.startswith('10') and i2b_3.startswith('10') and i2b_4.startswith('10'):
            print(1)
        else:
            print(0)

