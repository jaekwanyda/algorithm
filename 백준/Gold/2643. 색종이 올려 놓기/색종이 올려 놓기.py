import sys
input = sys.stdin.readline
#아이디어: 더 긴 길이를 가로로 고정하고 가장 큰거에서 차곡차곡 쌓기
#색종이 수 입력받기
n = int(input())
squares = []
for _ in range(n):
    a,b = map(int,input().split())
    if a<b:
        a,b = b,a
    squares.append((a,b))
#가로 길이 긴 것 순대로 넣기
squares = sorted(squares,key=lambda x:(-x[0],-x[1]))
dp = [1]*n
if n == 1:
    print(1)
else:
    for i in range(1,n):
        a = i-1
        while a>-1:
            if squares[a][1]>=squares[i][1]:
                dp[i] = max(dp[i],dp[a]+1)
            a -= 1
    print(max(dp))