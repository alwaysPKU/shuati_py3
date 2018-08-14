import sys


def judge(cash):
    duoyu=cash-5000
    if duoyu < 0:
        shui=0
    elif duoyu<=3000:
        shui=round(duoyu*0.03)
    elif duoyu>3000 and duoyu<=12000:
        shui=round(90.0+(duoyu-3000)*0.1)
    elif duoyu>12000 and duoyu<=25000:
        shui = round(990.0 + (duoyu-12000)+0.2)
    elif duoyu>25000 and duoyu<=35000:
        shui=round(3590.0+(duoyu-25000)*0.25)
    elif duoyu>35000 and duoyu<=55000:
        shui = round(6090.0 +(duoyu-35000)* 0.3)
    elif duoyu>55000 and duoyu<=80000:
        shui = round(12090.0 + (duoyu-55000)*0.35)
    else :
        shui = round(20840.0 + (duoyu-80000)*0.45)
    return shui

if __name__ == '__main__':
    num=int(sys.stdin.readline().rstrip())
    res=[]
    for i in range(num):
        sal=int(sys.stdin.readline().strip())
        res.append(judge(sal))
    for i in res:
        print(i)


