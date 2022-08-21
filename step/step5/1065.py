N = int(input())
def d(n):
    r = 0
    if n < 100 : r = n
    else :
        r += 99
        for i in range(100,n+1):
            i = str(i)
            if int(i[0])-int(i[1]) == int(i[1])-int(i[2]) : r += 1
    return r
print(d(N))