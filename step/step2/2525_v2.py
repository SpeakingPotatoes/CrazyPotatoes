a, b = input().split(' ')
c = input()

h = int(a)
m = int(b)
duration = int(c)

quotient = (m + duration) // 60
remainder = (m + duration) % 60

print((h + quotient) % 24, remainder)