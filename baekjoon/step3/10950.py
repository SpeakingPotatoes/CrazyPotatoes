l = int(input())
result = []
a = 0
b = 0
for i in range(l):
    i = input().split()
    a = int(i[0])
    b = int(i[1])
    result.append(a + b)
for i in result : print(i)