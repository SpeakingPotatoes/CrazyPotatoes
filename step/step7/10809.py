s = list(input())
res = [-1] * 26
alphabet = list('abcdefghijklmnopqrstuvwxyz')

for i in range(len(alphabet)) :
    for j in range(len(s)):
        if alphabet[i] == s[j] and  res[i] == -1 : res[i] = j

for i in res : print(i, end = ' ')
