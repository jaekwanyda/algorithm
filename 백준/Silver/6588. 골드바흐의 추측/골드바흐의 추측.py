import sys
input = sys.stdin.readline
#아이디어: 모든 경우의 홀수 소수로 만들어보자
primes = []
tmp = [0]*1000001
for i in range(2,1000+1):
    if tmp[i] == 0:
        for j in range(2*i,1000001,i):
            tmp[j] = i
for i in range(3,1000001):
    if tmp[i] == 0:
        primes.append(i)
primes_set = set(primes)
while True: 
    target = int(input())
    if target == 0:
        break
    found = False
    for p in primes:
        if target-p in primes_set:
            print(f'{target} = {p} + {target-p} ')
            found = True
            break
    if not found:
        print("'Goldbach's conjecture is wrong.")