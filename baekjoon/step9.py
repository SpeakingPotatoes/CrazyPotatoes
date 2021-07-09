#%% 1978 소수 판별
N = int(input())
n = input().split()

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
res = 0
for i in n:
    if int(i) in prime: res += 1
print(res)

#%% 2581

#%%
