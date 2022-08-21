T = int(input())
for i in range(T):
    res = 0
    move = 1
    tmp = input().split()
    x = int(tmp[0])
    y = int(tmp[1])
    d = y-x
    while True:
        d -= 2*move
        res += 2
        if d < 0:
            if abs(d) >= move: res -= 1
            break
        elif d == 0: break
        move += 1
    print(res)
