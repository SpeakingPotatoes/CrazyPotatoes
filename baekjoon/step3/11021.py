import sys
T = int(input())
result = []
for i in range(T):
    a = sys.stdin.readline().split()
    result.append(int(a[0]) + int(a[1]))
for i in range(T):
    print("Case #%d: %d" %(i+1,result[i]))