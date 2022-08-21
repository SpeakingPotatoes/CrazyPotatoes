a = input()
if len(a) == 1 : a = "0" + a
result = a
i = 0

while True:
    a10 = int(a[0])
    a1 = int(a[1])
    temp10 = a1
    temp1 = a10 + a1
    if temp1 >= 10 : temp1 -=10
    a = str(temp10) + str(temp1)
    i = i + 1
    if result == a : break
print(i)