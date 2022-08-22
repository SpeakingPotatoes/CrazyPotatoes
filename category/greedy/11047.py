#%%
import sys
n, k = map(int, input().split(" "))

a_lst = []
for _ in range(n):
    a_lst.append(sys.stdin.readline())
a_lst.reverse()

num = 0
for a in a_lst:
    while a <= k:
        k -= a
        num += 1
print(num)
