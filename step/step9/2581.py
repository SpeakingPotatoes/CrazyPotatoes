#%%
import math

M = int(input())
N = int(input())

res_lst = []

for i in range(M, N+1):
    tmp = 1
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0 : 
            tmp = 0
            break
    if tmp == 1 : res_lst.append(i)
if 1 in res_lst: res_lst.remove(1)
if res_lst == []: print(-1)
else:
    print(sum(res_lst), min(res_lst), sep = '\n')
# %%