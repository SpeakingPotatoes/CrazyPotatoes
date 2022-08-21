n1 = int(input())
n2 = []
a = int(input())
a_100 = a // 100
n2.append(a_100)
a_10 = (a - a_100 * 100)//10
n2.append(a_10)
a_1 = (a - a_100 * 100 - a_10 * 10) // 1
n2.append(a_1)
n2.reverse()
result = 0
for i in range(len(n2)):
    mul_sum = 0 
    mul_sum = n1 * n2[i]
    result += mul_sum * 10 ** i
    print(mul_sum)
print(result)