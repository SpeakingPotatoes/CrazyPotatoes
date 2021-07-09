a = input().split()
for i in range(0,len(a)): a[i] = int(a[i])

sum = a[0]
sub = a[0]
mul = a[0]
div = a[0]
div2 = a[0]

for i in range(1,len(a)): sum += a[i]
print(sum)

for i in range(1,len(a)):
    sub -= a[i]
    abs(sub)
print(sub)

for i in range(1,len(a)): mul *= a[i]
print(mul)

for i in range(1,len(a)): div /= a[i]
print(int(div))

for i in range(1,len(a)): div2 %= a[i]
print(div2)