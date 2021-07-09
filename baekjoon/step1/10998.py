a = input().split()
for i in range(0,len(a)): a[i] = int(a[i])
mul = a[0]
for i in range(1,len(a)): mul *= a[i]
print(mul)