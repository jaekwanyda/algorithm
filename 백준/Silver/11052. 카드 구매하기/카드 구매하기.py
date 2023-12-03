import sys
input = sys.stdin.readline
#아이디어: dp로 해결하자
n = int(input())
cards = [0] + list(map(int,input().split()))
dp = cards[:]
for i in range(1,n+1):
    for j in range(1,i):
        dp[i] = max(dp[i],dp[i-j]+dp[j])
print(dp[-1])