n = 0
while n<1 or n>100:
	n = int(input())
for i in range(1,n+1):
	print("%s%s"%(" "*(n-i),"*"*i))
