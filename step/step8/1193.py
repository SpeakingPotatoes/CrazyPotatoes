# 1th : 합이2 1
# 2th : 합이3 2~3
# 3th : 합이4 4~6
# 4th : 합이5 7~10
# 5th : 합이6 11~15
X = int(input())
i = 1
while True:
    if i >= X : break
    else:
        X -= i
        i += 1
if i%2 == 0 : res = [X, i+1-X]
else : res = [i+1-X, X]
print("%d/%d" %(res[0],res[1]))
