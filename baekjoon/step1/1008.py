a = input().split()
for i in range(0,len(a)): a[i] = float(a[i])
div = a[0]
for i in range(1,len(a)): div /= a[i]
print(div)