t = int(input())

num = []
while True:
    if len(num) == t: break
    _ = int(input())
    num.append(_)


n = 10000
a = [True] * (n+1)

for i in range(2, int(n**0.5 + 1)):
    if a[i] == True:
        for j in range(i + i, n + 1, i):
            a[j] = False

prime_num = [i for i in range(2, n+1) if a[i] == True]


for n_ in num:
    under_prime = [x for x in prime_num if x <= n_]
    
    comb = []
    for u in under_prime:
        for w in under_prime[under_prime.index(u):]:
            if u + w == n_:
                comb.append((u, w))

    subt = [abs(x[0]-x[1]) for x in comb]
    idx = subt.index(min(subt))
    print(comb[idx][0], comb[idx][1])


# for n_ in num:
#     under_prime = [x for x in prime_num if x <= n_]
#     comb = list(combinations_with_replacement(under_prime, 2))
#     idx = [i for i in range(len(comb)) if list(map(sum, comb))[i] == n_]

#     if len(idx) == 1:
#         print(comb[idx[0]][0], comb[idx[0]][1])

#     else:
#         subt = [abs(x[0]-x[1]) for x in comb if comb.index(x) in idx]
#         i_ = subt.index(min(subt))
#         print(comb[idx[i_]][0], comb[idx[i_]][1])
