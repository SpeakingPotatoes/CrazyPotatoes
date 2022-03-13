#%%
N, K = map(int, input().split())
A = []
for _ in range(N):
    A = [int(input())] + A
res = 0
idx = 0
while K != 0:
    if K // A[idx] == 0 : idx += 1
    else:
        K -= A[idx]
        res += 1
print(res)
# %%
