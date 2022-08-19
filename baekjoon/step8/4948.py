#%%
'''
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 
'''
import sys


def prime_check(num):
    chkr = 1
    for i in range(int(num**(1/2)), 1, -1):
        if num % i == 0:
            # print(i)
            chkr = 0
            break

    return chkr
# prime_check(100)
# for i in range(10, 1, -1): print(i)

# n_lst = []
while True:
    n = int(sys.stdin.readline())
    if n == 0: break
    prime_num = 0
    for i in range(n+1, 2*n+1):
        chkr = prime_check(i)
        prime_num += chkr
    print(prime_num)
    # n_lst.append(n)
'''
n_lst = [1, 10, 13, 100, 1000, 10000, 100000]
for n in n_lst:
    n = 123456
    prime_num = 0
    for i in range(n+1, 2*n+1):
        chkr = prime_check(i)
        prime_num += chkr
    print(prime_num)
'''