import sys
input = sys.stdin.readline
#아이디어: dp
n,m = map(int,input().split())
mega = list(map(int,input().split()))
cancel = list(map(int,input().split()))
dp = [[0]*(sum(cancel)+1) for _ in range(n)]
for i in range(cancel[0],sum(cancel)+1):
    dp[0][i] = mega[0]
for i in range(1,n):
    for j in range(sum(cancel)+1):
        if j >= cancel[i]:
            dp[i][j] = max(dp[i][j],dp[i-1][j-cancel[i]] + mega[i])
        dp[i][j] = max(dp[i][j],dp[i-1][j])
for i in range(sum(cancel)+1):
    if dp[n-1][i] >= m:
        print(i)
        break