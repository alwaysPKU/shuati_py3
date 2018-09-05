import sys

if __name__ == '__main__':
    hp=int(sys.stdin.readline().rstrip())
    na=int(sys.stdin.readline().rstrip())
    ba=int(sys.stdin.readline().rstrip())
    zheng=0
    if na*2>=ba:
        zheng=hp//na
        yu=hp%na
        if yu != 0 :
            zheng+=1
        # print(zheng)
    else:
        zheng=hp//ba
        yu=hp%ba
        if yu == 0:
            zheng*=2
        else:
            yu2=yu//na
            yu3=yu%na
            if yu3 != 0:
                zheng=zheng*2+yu2+1
            else:
                zheng=zheng*2+yu2
    print(zheng)