#coding=utf-8
import sys
import datetime


def get_time(q):
    time = datetime.datetime.strptime(q, '%H:%M:%S')
    time2 = datetime.datetime.strptime('00:00:00', '%H:%M:%S')
    dela = time - time2
    return int(dela.total_seconds())


def re():
    num_time = int(sys.stdin.readline().strip())
    weeks = []
    times = []
    time_list = []
    weeks_new = []
    times_new = []
    time_list_new = []
    for i in range(num_time):
        line = sys.stdin.readline().strip().split(' ')
        weeks.append(int(line[0]))
        times.append(int(line[1]))
        time_list.append(line[2:])
    for w, t, tl in sorted(zip(weeks, times, time_list), key=lambda x: x[0]):
        weeks_new.append(w)
        times_new.append(t)
        time_list_new.append(tl)
    num_query = int(sys.stdin.readline().strip())
    query_week = []
    query_time = []
    for i in range(num_query):
        line = sys.stdin.readline().strip().split(' ')
        query_week.append(int(line[0]))
        query_time.append(line[1])
    for w, t in query_week, query_time:
        ind = 0
        mark = 0
        for index, i in weeks_new:
            if w < i:
                ind = index
            elif w == i:
                mark = 1
                ind = index
            else:
                break
        # m2=0
        if mark:
            m2 = 0
            ti = time_list_new[ind]
            for tii in ti:
                tmp = tii.split('-')
                t1 = tmp[0]
                t2 = tmp[1]
                t11 = get_time(t1)
                t22 = get_time(t2)
                if get_time(t) >= t11 and get_time(t) <= t22:
                    print(0)
                    m2 = 1
                    break
            if not m2:
                delta_week = weeks_new[ind + 1] - w - 1
                ab = delta_week * 24 * 60 * 60
                print(get_time(time_list_new[ind + 1][0].split('-')[0]) + 24 * 60 * 60 - get_time(t) + ab)

        else:
            delta_week = weeks_new[ind + 1] - w - 1
            ab = delta_week * 24 * 60 * 60
            print(get_time(time_list_new[ind + 1][0].split('-')[0]) + 24 * 60 * 60 - get_time(t) + ab)
if __name__ == '__main__':
    example=int(sys.stdin.readline().strip())
    for i in range(example):
        re()







