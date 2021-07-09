n = int(input())
result = []


for i in range(n):
    k = 0
    temp = 0
    a = input()
    for j in range(len(a)):
        if a[j] =="O" :
            k += 1
            temp += k 
        elif a[j] == "X": k =0
    result.append(temp)
for i in result: print(i)