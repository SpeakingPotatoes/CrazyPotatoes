from itertools import combinations

n, m = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))

s_ = list(map(lambda x: sum(x), list(combinations(cards, 3))))

print(max(i for i in s_ if i <= m))
