a = input().upper()
d = dict()
for i in range(len(a)):
    if a[i] in d : d[a[i]] += 1
    else : d[a[i]] = 1
M = max(d.values())
res = 0
for i in d.values() :
    if i == M :
        res += 1
if res >= 2:print("?")
else: 
    for key, value in d.items():
        if value == M:
            print(key)
