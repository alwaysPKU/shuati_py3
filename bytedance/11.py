a =  [ [1,2,3],[4,5,6],[3,4],[7,8],[8,9],[6,12,13] ]
b = len(a)
for i in range(b):
    for j in range(b):
        x = list(set(a[i]+a[j]))
        y = len(a[j])+len(a[i])
        if i == j or a[i] == 0 or a[j] == 0:
            break
        elif len(x) < y:
            a[i] = x
            a[j] = [0]
        print (a)

print ([i for i in a if i != [0]])