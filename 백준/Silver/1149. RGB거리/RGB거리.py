import sys
input = sys.stdin.readline
#아이디어: 색깔 별로 가장 작은 값을 저장해주자
#n 입력받기
n = int(input())
color = [list(map(int,input().split())) for _ in range(n)]
dp = [[0,0,0] for _ in range(n)]
dp[0] = color[0] #첫번째는 그대로
for i in range(n):
    #이번 색 R
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + color[i][0]
    #이번 색 G
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + color[i][1]
    #이번 색 B
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + color[i][2]
print(min(dp[n-1]))
