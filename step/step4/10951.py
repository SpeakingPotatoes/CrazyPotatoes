import sys
result = []

while True:
    a = sys.stdin.readline().split()
    if a == []: break
    b = int(a[0]) + int(a[1])
    result.append(b)
for i in result : print(i)