import sys
res = []
while True:
    s = sys.stdin.readline().split()
    if s == [] : break
    r = int(s.pop(0))    
    p = ''
    for i in s :
        for j in range(len(i)): p += i[j]*r
    if s != []: res.append(p)
for i in res: print(i)
