n = input().split()
A = n[0]
B = n[1]
A = int(A[0]) + int(A[1])*10 + int(A[2])*100
B = int(B[0]) + int(B[1])*10 + int(B[2])*100
if A > B : print(A)
else: print(B)
