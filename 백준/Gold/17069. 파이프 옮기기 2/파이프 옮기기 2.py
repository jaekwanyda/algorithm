import sys
input = sys.stdin.readline
#아이디어: 단순히 파이프 방향에 따른 구현을 하고 bfs를 돌리면 될 것 같다
#=>근데 시간이 오래 걸려 n 별로 dp를 구현해보자
#n 입력받기
n = int(input())
#array 입력받기
array = [list(map(int,input().split())) for _ in range(n)]
pipe = ((0,2),(1,2),(0,1,2)) #0은 가로 -> (가로,대각), 세로 ->(세로,대각),대각=>(전부)
dx = [0,1,1];dy=[1,0,1]
#가로 세로 대각 정보를 담는 dp 생성
dp = [[[0,0,0] for i in range(n)]for _ in range(n)]
#시작지점은 0,1 과 방향 가로로 하나 추가해주기
dp[0][1][0] = 1
for i in range(n):
    for j in range(1,n):
        #dp 에서 갈 수 있는 지점에 방향과 정보 더해주기
        if array[i][j] == 0: #갈 수 있을 때만 진행
            #가로 방향으로 진행
            if j+1<n and array[i][j+1] == 0:
                dp[i][j+1][0] += dp[i][j][0] + dp[i][j][2]
            #세로 방향으로 진행
            if i+1<n and array[i+1][j] == 0:
                dp[i+1][j][1] += dp[i][j][1] + dp[i][j][2]
            if i+1<n and j+1<n and array[i+1][j] == 0 and array[i][j+1] ==0 and array[i+1][j+1] == 0:
                dp[i+1][j+1][2] += dp[i][j][0] + dp[i][j][1] +dp[i][j][2]
          

print(sum(dp[n-1][n-1]))