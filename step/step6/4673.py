def d(n):
    sum = n
    s = str(n)
    for i in range(len(s)): 
        sum += int(s[i])
    return sum

result = []
com = []
for i in range(10000): 
    result.append(i+1)
    com.append(d(i+1))
result = list(set(result) - set(com))
result.sort()
for i in result : print(i)