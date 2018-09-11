import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    print(nums)
    bt = b''

    for num in nums:
        bt += num.to_bytes(1, byteorder='big')
    print(bt)
    try:
        bt.decode('utf8')
        print(1)
    except Exception as e:
        print(0)
