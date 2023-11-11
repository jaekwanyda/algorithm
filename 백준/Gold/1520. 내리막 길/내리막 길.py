import sys
input = sys.stdin.readline
#아이디어: dp와 heapq로 해결해보자
import heapq
n,m = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
dx = [0,0,-1,1]
dy = [-1,1,0,0]
dp = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dp[0][0] = 1
q = []
heapq.heappush(q,[-array[0][0],0,0]) #최대 힙
while q:
    cnt,x,y = heapq.heappop(q)
    if visited[x][y]:
        continue
    visited[x][y] = 1
    cnt *= -1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<m and array[x][y] > array[nx][ny] and not visited[nx][ny]:
            dp[nx][ny] += dp[x][y]
            heapq.heappush(q,[-array[nx][ny],nx,ny])
print(dp[n-1][m-1])