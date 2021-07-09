a = input().split()
for i in range(0,len(a)): a[i] = int(a[i])
A = a[0]
B = a[1]
C = a[2]
result = [(A+B)%C,((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C]
for i in result :  print(i)