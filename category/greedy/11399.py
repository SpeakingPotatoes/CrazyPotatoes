N = int(input())
p_lst = list(map(int, input().split(" ")))
p_lst.sort()
res = [sum(p_lst[0:i+1]) for i in range(len(p_lst))]
print(sum(res))
