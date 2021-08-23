#%%
import math

N = int(input())
res = []

for i in range(2, int(math.sqrt(i))+1):
    if N % i == 0 :
        N = N \ i
        res.append(i)
        
# %%

