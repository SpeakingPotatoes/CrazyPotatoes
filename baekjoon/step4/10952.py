result = []
while True: 
    a = input().split()
    if a == ["0","0"]: break
    b = int(a[0]) + int(a[1])
    result.append(b)
for i in result : print(i)