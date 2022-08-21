a = input()
a = a.split()
sub = int(a[0])
for i in range(1,len(a)):
    sub -= int(a[i])
    abs(sub)
print(sub)