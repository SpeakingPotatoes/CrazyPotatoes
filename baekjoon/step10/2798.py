#%%
n, m = map(int, input().split(" "))
n_lst = list(map(int, input().split(" ")))

res = []
for i in range(len(n_lst)):
    n_lst_1 = n_lst.copy()
    n1 = n_lst_1.pop(i)
    for j in range(len(n_lst_1)):
        n_lst_2 = n_lst_1.copy()
        n2 = n_lst_2.pop(j)
        for n3 in n_lst_2:
            res.append(n1+n2+n3)

print(m - min([m - num for num in res if m - num >= 0]))




