import sys
input = sys.stdin.readline
#아이디어: 소수를 모두 찾고 모든 경우의 수를 확인해주자
def answer():
    n = int(input())
    if n == 1:
        print(0)
        return
    primes = []
    check = [0]*(n+1)
    for i in range(2,n+1):
        if check[i] == 0:
            primes.append(i)
            a = i
            while a < n+1:
                check[a] = i
                a += i
    primes_partial_sum = [0]*(len(primes)+1)
    for i in range(1,len(primes)+1):
        primes_partial_sum[i] += primes[i-1] + primes_partial_sum[i-1]
    result = 0
    primes_partial_sum_set = set(primes_partial_sum)
    for p_p in primes_partial_sum:
        if p_p - n in primes_partial_sum_set:
            result += 1
    print(result)
    return
answer()