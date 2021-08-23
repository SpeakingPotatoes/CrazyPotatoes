#%%
import math

N = int(input())
n = input().split()
res = 0
one = 0
for i in n:
    if int(i) == 1 : one = -1
    tmp = 0
    for j in range(2, int(math.sqrt(int(i)))+1):
        if int(i) % j  == 0 : tmp = 1
    if tmp == 0 : res += 1

print(res + one)
# %%
N = int(input())
n = input().split()
res = 0
one = 0
for i in n:
    if int(i) == 1 : one = -1 
    tmp = 0 
    for j in range(2,int(i)):
        if int(i) % j == 0 : tmp = 1
    if tmp == 0 : res += 1
    
print(res + one)
# %%