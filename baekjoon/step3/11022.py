import sys
result = []
num1 = []
num2 = []
T = int(input())
for i in range(T):
    a = sys.stdin.readline().split()
    num1.append(int(a[0]))
    num2.append(int(a[1]))
    result.append(num1[i] + num2[i])
for i in range(T):print("Case #%d: %d + %d = %d" %(i+1,num1[i],num2[i],result[i]))