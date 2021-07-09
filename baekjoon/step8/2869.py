N = input().split()
A = int(N[0])
B = int(N[1])
V = int(N[2]) - A
res = 1
res += V // (A-B)
if V % (A-B) != 0 :  res += 1

