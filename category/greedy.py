#%% 곱하기 혹은 더하기
S = input()

res = 0
for i in S:
    if int(i) <= 1 or res <=1 : res += int(i)
    else : res *= int(i)
print(res)
# %%
