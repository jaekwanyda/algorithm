import sys
input = sys.stdin.readline
#아이디어:체를 이용해서 소수 리스트를 구현하고 거기서 팰린드롭인지 확인
#팰린드롭인지 확인해주는 함수
def palindrom(k):
    if int(str(k)[::-1])==k:
        return True
    return False
#n입력받기
n = int(input())
m=2000000
primes = [False,False] + [True]*(m-1)
for i in range(2,m+1):
  if primes[i]:
    for j in range(2*i, m+1, i):
        primes[j] = False
while True:
   if primes[n] == True and palindrom(n):
      print(n)
      break
   else:
      n+=1