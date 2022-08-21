#%%
M, N = input().split()
M = int(M)
N = int(N)
#%%
# M, N = 3, 16
for i in  range(M, N + 1):
    is_decimal = 1
    i_ = 2
    while i_ != i:
        if i % i_ == 0: 
            is_decimal = 0
            break
        i_ += 1
    if is_decimal == 1: print(i)
# %%
tmp = [i for i in range(3, 17)]
#%%
M = 10
res = []
for i in  range(M, 2*M+1):
    is_decimal = 1
    for j in range(2, i):
        if i % j == 0: is_decimal = 0
    if is_decimal == 1: res.append(i)
print(len(res))
# %%
