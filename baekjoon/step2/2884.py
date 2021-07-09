a = input().split()
h = int(a[0])
m = int(a[1])
result_m = m - 45
result_h = h
if result_m < 0 :
    result_m = 60 - abs(result_m)
    result_h = h - 1
    if result_h <0 : result_h = 23
print(result_h, result_m)