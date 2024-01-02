import sys
input = sys.stdin.readline
#아이디어: dp
n = int(input())
array_sizes = []
for _ in range(n):
    a,b = map(int,input().split())
    array_sizes.append((a,b))
dp = [[0]*n for _  in range(n)]
for length in range(1,n): #행렬 계산 크기
    for i in range(n): #계산 시작 지점
        if i + length == n:
            break
        dp[i][i+length] = float('inf') #가장 큰 수로 초기화
        for j in range(i, i+length):
            dp[i][i+length] = min(dp[i][i+length], dp[i][j]+dp[j+1][i+length] + array_sizes[i][0] * array_sizes[j][1] * array_sizes[i+length][1])

print(dp[0][n-1])   