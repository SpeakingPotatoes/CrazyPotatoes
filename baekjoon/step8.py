# %% 1712
N = input().split()
A = int(N[0])
B = int(N[1])
C = int(N[2])
if C <= B :  res = -1
else: res = A // (C-B) + 1
print(res)

# %% 2292
#첫번째방 1
#두번째방 2~7 : 6개
#세번째방 8~19 : 12개
#네번재방 20~37 : 18개
#다섯번째방 38~63 : 24개
N = int(input())
temp = ((N+4) // 6) 
i = 1
while temp > 0:
    temp -= i
    i += 1
print(i)

#%% 1193
# 1th : 합이2 1
# 2th : 합이3 2~3
# 3th : 합이4 4~6
# 4th : 합이5 7~10
# 5th : 합이6 11~15
X = int(input())
i = 1
while True:
    if i >= X : break
    else:
        X -= i
        i += 1
if i%2 == 0 : res = [X, i+1-X]
else : res = [i+1-X, X]
print("%d/%d" %(res[0],res[1]))

# %% 2869
N = input().split()
A = int(N[0])
B = int(N[1])
V = int(N[2]) - A
res = 1
res += V // (A-B)
if V % (A-B) != 0 :  res += 1

print(res)

#%% 10250
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

#%% 2775
res = []
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    temp = [i+1 for i in range(n)]
    for j in range(k):
        temp = [sum(temp[0:i+1]) for i in range(n)]
    print(temp[-1])

#%% 2839
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

# %% 10757
AB = input().split()
print(int(AB[0])+int(AB[1]))

#%% 1011
T = int(input())
for i in range(T):
    res = 0
    move = 1
    tmp = input().split()
    x = int(tmp[0])
    y = int(tmp[1])
    d = y-x
    while True:
        d -= 2*move
        res += 2
        if d < 0:
            if abs(d) >= move: res -= 1
            break
        elif d == 0: break
        move += 1
    print(res)
    
# %%
