from collections import Counter

a, b, c = map(int, input().split(' '))
count = Counter([a, b, c])

if len(count) == 1:
    print(10000 + count.most_common(1)[0][0] * 1000)
    
elif len(count) == 2:
    print(1000 + count.most_common(1)[0][0] * 100)

else:
    print(max(a, b, c) * 100)
