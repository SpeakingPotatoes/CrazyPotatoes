T = int(input())
res = []
for i in range(T):
    temp = input().split()
    H = int(temp[0])
    W = int(temp[1])
    N = int(temp[2])

    R = N // H + 1 
    F = N % H
    if F == 0 : 
        R -= 1
        F = H  
    F = str(F)
    R = str(R)
    if len(R) == 1 : R = "0" + R
    room_num = F + R  
    res.append(room_num)

for i in range(T):print(res[i])
