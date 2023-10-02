import sys
input = sys.stdin.readline
#아이디어: dp를 이용해 0~9로 시작하는 이전 자리수를 이용해보자
from collections import defaultdict
#t 입력받기
t = int(input())
dp = [defaultdict(int) for _ in range(65)]
dp[1][0]=dp[1][1]=dp[1][2]=dp[1][3]=dp[1][4]=dp[1][5]=dp[1][6]=dp[1][7]=dp[1][8]=dp[1][9] = 1
for i in range(2,65):
    for j in range(0,10):
        for k in range(j,10):
            dp[i][j] += dp[i-1][k]
for _ in range(t):
    #n 입력받기
    n = int(input())
    print(sum(dp[n].values()))