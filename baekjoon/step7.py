#%% 11654
print(ord(input()))

#%% 11720
n = int(input())
N = input()
res = 0
for i in range(n): 
    res += int(N[i])
print(res)


#%% 10809
s = list(input())
res = [-1] * 26
alphabet = list('abcdefghijklmnopqrstuvwxyz')

for i in range(len(alphabet)) :
    for j in range(len(s)):
        if alphabet[i] == s[j] and  res[i] == -1 : res[i] = j

for i in res : print(i, end = ' ')

#%% 2675
import sys
res = []
while True:
    s = sys.stdin.readline().split()
    if s == [] : break
    r = int(s.pop(0))    
    p = ''
    for i in s :
        for j in range(len(i)): p += i[j]*r
    if s != []: res.append(p)
for i in res: print(i)

#%% 1157
a = input().upper()
d = dict()
for i in range(len(a)):
    if a[i] in d : d[a[i]] += 1
    else : d[a[i]] = 1
M = max(d.values())
res = 0
for i in d.values() :
    if i == M :
        res += 1
if res >= 2:print("?")
else: 
    for key, value in d.items():
        if value == M:
            print(key)
            
#%% 1152
a = input().split()
print(len(a))

#%% 2908
n = input().split()
A = n[0]
B = n[1]
A = int(A[0]) + int(A[1])*10 + int(A[2])*100
B = int(B[0]) + int(B[1])*10 + int(B[2])*100
if A > B : print(A)
else: print(B)

#%% 5622
dial = {'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':9}
a = input()
res = 0
for i in range(len(a)):
    temp = a[i]
    res += dial[temp] + 1
print(res)

# %% 2941
a = input()
res = 0
croatia_1 = ['=','-']
croatia_2 = ['n','l']
temp = ''
for i in range(len(a)):
    res += 1
    if a[i] in croatia_1 :
        res -= 1
        if temp == 'z' and a[i-2] == 'd' : res -= 1
    elif a[i] == 'j' and temp in croatia_2 : res -=1

    temp = a[i]
print(res)

# %% 1316
import sys

N = int(input())
res = 0

for i in range(N):
    gw = dict()
    a = sys.stdin.readline()
    isgw = 1
    temp = a[0]
    for j in range(len(a)):
        if a[j] not in gw:
            gw[a[j]] = 1
        else:
            if temp == a[j] :
                gw[a[j]] += 1
            else :
                isgw = 0
        temp = a[j]
    if isgw == 1 : res += 1
print(res)
