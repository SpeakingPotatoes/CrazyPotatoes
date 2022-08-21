N = input().split()
A = int(N[0])
B = int(N[1])
C = int(N[2])
if C <= B :  res = -1
else: res = A // (C-B) + 1
print(res)