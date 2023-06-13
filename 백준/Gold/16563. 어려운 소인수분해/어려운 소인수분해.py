import sys
from collections import deque
input = sys.stdin.readline
#아이디어: 체를 만들어서 5000000보다 작은 소수를 담은 list를 만들고 N을 계속 나눠준다.
#n 입력받기
n = int(input())
#자연수 입력받기
array = list(map(int,input().split()))
m = max(array)
#체 만들기
spf = [0]*(m+1)
prime_set = []
for i in range(2, m+1):
    if not spf[i]:
        prime_set.append(i)
        spf[i] = i			
    for p in prime_set:
        if i * p > m:
            break
        spf[i*p] = p			
        if i % p == 0:
            break
for i in array:
    a = [spf[i]]
    while i > 1:
        i //= spf[i]
        if i!=1:
            a.append(spf[i])
    a.sort()
    print(*a)

