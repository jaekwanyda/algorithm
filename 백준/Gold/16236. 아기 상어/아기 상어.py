import sys
input = sys.stdin.readline
from collections import deque
#아이디어: bfs
n = int(input())
shark_x = 0
shark_y = 0
array = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            shark_x,shark_y = i,j
            array[shark_x][shark_y] = 0
shark_size = 2
grow = shark_size
answer = 0
dx = [-1,0,0,1]
dy = [0,-1,1,0]
while True:
    target_x,target_y = -1,-1
    q = deque()
    visited = [[0]*n for _ in range(n)]
    visited[shark_x][shark_y]= 1
    q.append((shark_x,shark_y,0))
    fix_d = -1
    result = []
    while q:
        x,y,d = q.popleft()
        if fix_d > 0 and fix_d != d+1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and array[nx][ny] <= shark_size and not visited[nx][ny]:
                if array[nx][ny] and array[nx][ny] < shark_size:
                    fix_d = d+1
                    result.append((nx,ny))
                visited[nx][ny] = 1
                q.append((nx,ny,d+1))
    if not result:
        break
    grow -= 1
    if not grow:
        shark_size += 1
        grow = shark_size
    answer += fix_d
    result = sorted(result,key = lambda x:(x[0],x[1]))
    shark_x,shark_y = result[0][0],result[0][1]
    array[shark_x][shark_y] = 0
print(answer)
