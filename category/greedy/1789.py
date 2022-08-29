#%%
s = int(input())
num = 0
res = 0
nums = []
while True:
    num += 1
    s -= num
    if s <= num:
        s += num
        nums.append(s)
        break
    else: 
        nums.append(num)
print(len(nums))