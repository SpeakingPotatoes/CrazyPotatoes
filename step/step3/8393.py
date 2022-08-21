n = 0
while n<1 or n>10000:
	n = int(input())
sum = 0
for i in range(1,n+1):
	sum = sum + i
print (sum)