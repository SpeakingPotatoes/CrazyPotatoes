A, B = map(int, input().split(" "))
C = int(input())

quot = B + C // 60
m = B + C % 60
h = A + quot
if h >= 24: h -= 24

print(h, m)