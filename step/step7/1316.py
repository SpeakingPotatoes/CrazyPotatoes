import sys

N = int(input())
res = 0

for i in range(N):
    gw = dict()
    a = sys.stdin.readline()
    isgw = 1
    temp = a[0]
    for j in range(len(a)):
        if a[j] not in gw:
            gw[a[j]] = 1
        else:
            if temp == a[j] :
                gw[a[j]] += 1
            else :
                isgw = 0
        temp = a[j]
    if isgw == 1 : res += 1
print(res)
