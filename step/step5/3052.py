l = []
a = 0
for i in range(10):
    a = int(input())
    l.append(a%42)
result = set(l)
print(len(result))