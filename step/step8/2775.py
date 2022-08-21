res = []
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    temp = [i+1 for i in range(n)]
    for j in range(k):
        temp = [sum(temp[0:i+1]) for i in range(n)]
    print(temp[-1])
