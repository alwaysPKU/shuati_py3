import sys

if __name__ == '__main__':
    num = int(sys.stdin.readline())
    for i in range(num):
        t=sys.stdin.readline().rstrip()
        t_list=t.split(':')
        # print(t_list)
        for i,t in enumerate(t_list):
            # print(i,t)
            if i==0 and int(t)>23:
                t_list[i]='0'+t[1]
                # print('>>',t_list[0])
            if i>0 and int(t)>59:
                t_list[i]='0'+t[1]
        res=':'.join(t_list)
        print(res)