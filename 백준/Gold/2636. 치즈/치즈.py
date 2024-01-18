import sys
input = sys.stdin.readline
from collections import deque
#아이디어: 한시간 마다 처리해주자
n,m = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]
melt_cheese = [[0]*m for _ in range(n)]
hour = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while True:
    hour += 1
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if array[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))
            elif array[nx][ny]:
                melt_cheese[nx][ny] = 1
    if melt_cheese == array:
        print(hour)
        print(sum(sum(melt) for melt in melt_cheese))
        break
    for i in range(n):
        for j in range(m):
            array[i][j] -= melt_cheese[i][j]
    melt_cheese = [[0]*m for _ in range(n)]
