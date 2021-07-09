c = int(input())
result = []
for i in range(c):
    temp = []
    over = 0
    avg = 0
    a = input().split()
    n = int(a[0])
    for j in range(1,n+1):
        temp.append(int(a[j]))
        avg += int(a[j])
    avg /= n
    for j in temp: 
        if j > avg : 
            over += 1
    result.append(over/n)
for i in result: print("{:<.3f}%".format(i * 100))