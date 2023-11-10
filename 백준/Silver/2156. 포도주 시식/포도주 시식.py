import sys
input = sys.stdin.readline
#아이디어: dp로 해결하자
n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))
dp = [0]*n
dp[0] = wine[0] #이번 잔 안먹은 경우, 이번 잔만 마신 경우, 이번 잔 전 잔까지 먹은 경우
if n>=2:
    dp[1] = wine[0]+wine[1]
if n>=3:
    dp[2] = max(dp[1],wine[0]+wine[2],wine[1]+wine[2])
if n>=4:
    for i in range(3,n):
        dp[i] = max(dp[i-1],dp[i-2]+wine[i],dp[i-3] + wine[i-1] + wine[i])
print(dp[-1])