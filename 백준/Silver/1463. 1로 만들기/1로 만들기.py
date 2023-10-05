import sys
input = sys.stdin.readline
#아이디어: DP를 이용하자
#n 입력받기
n = int(input())
#dp 생성
dp = [float('inf')]*(max(n+1,4))
dp[1] = 0
dp[2] = dp[3] = 1
for i in range(4,max(n+1,4)):
    if i%3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i%2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
    dp[i] = min(dp[i],dp[i-1]+1)
print(dp[n])