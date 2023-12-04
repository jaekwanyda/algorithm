import sys
input = sys.stdin.readline
#아이디어: 불이 날 시간들을 미리 계산해 graph에 넣어두자
from collections import deque
n,m = map(int,input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
fire_list = []
for i in range(n):
    tmp = list(input())
    graph.append(tmp)
    if 'J' in tmp:
        jihun_x = i
        jihun_y = tmp.index('J')
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            fire_list.append([i,j])
fire_visited = [[0]*m for _ in range(n)]
fire = deque()
for fire_x,fire_y in fire_list:
    fire.append([fire_x,fire_y,0])
    fire_visited[fire_x][fire_y] = True
#불 이동 기록
while fire:
    x,y,t = fire.popleft()
    graph[x][y] = t
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and not fire_visited[nx][ny] and graph[nx][ny] != "#":
            fire_visited[nx][ny] = True
            fire.append([nx,ny,t+1])
visited = [[0]*m for _ in range(n)]
q = deque()
q.append([jihun_x,jihun_y,0])
visited[jihun_x][jihun_y] = True
possible = False
#지훈이 이동시켜주기
while q:
    x,y,t = q.popleft()
    if x == 0 or y ==0 or x == n-1 or y == m-1:
        possible = True
        print(t+1)
        break
    graph[x][y] = t
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] != "#":
            if graph[nx][ny] == '.':
                visited[nx][ny] = True
                q.append([nx,ny,t+1])
            else:
                if t+1<graph[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx,ny,t+1])  
                    
if not possible:
    print('IMPOSSIBLE')