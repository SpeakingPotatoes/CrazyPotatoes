a = input()
res = 0
croatia_1 = ['=','-']
croatia_2 = ['n','l']
temp = ''
for i in range(len(a)):
    res += 1
    if a[i] in croatia_1 :
        res -= 1
        if temp == 'z' and a[i-2] == 'd' : res -= 1
    elif a[i] == 'j' and temp in croatia_2 : res -=1

    temp = a[i]
print(res)
