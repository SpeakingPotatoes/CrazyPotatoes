N = int(input())

list5 = range(N//5 + 1)
list3 = range(N//3 + 1)
res = -1

for i in reversed(list5):
    for j in reversed(list3):
        try:
            temp = i*5 + j*3
            if temp > N: continue
            elif N % (temp) == 0:
                res = i + j
                break
        except: continue
    if res != -1 : break
print(res)
