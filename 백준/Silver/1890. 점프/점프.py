import sys
input = sys.stdin.readline
#아이디어: dp로 해결하자
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if array[i][j]:
            ni = array[i][j] + i
            nj = array[i][j] + j
            if ni < n:
                dp[ni][j] += dp[i][j]
            if nj < n:
                dp[i][nj] += dp[i][j]
print(dp[-1][-1])