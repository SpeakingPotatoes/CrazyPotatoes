a = input().split()
n = int(a[0])
x = int(a[1])
b = input().split()
result = []
for i in range(n):
    b[i] = int(b[i])
    if b[i] < x :
        result.append(b[i])
for i in result: print(i,end=' ')