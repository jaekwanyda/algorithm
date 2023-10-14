import sys
input = sys.stdin.readline
#아이디어: 피사노 주기를 이용하자
n = int(input())
n = n%1500000
a,b = 1,1
cnt = 2
while cnt<n:
    a,b = b,(a+b)%1000000
    cnt += 1
print(b)