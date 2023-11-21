import sys
input = sys.stdin.readline
#아이디어: 단순한 DP 문제이다.
n,k = map(int,input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()
dp = [0]*(k+1)
dp[0] = 1
for num in nums:
    for i in range(num,k+1):
        dp[i] += dp[i-num]
print(dp[-1])
