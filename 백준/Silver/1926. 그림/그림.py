import sys
input = sys.stdin.readline
#아이디어: 1인 지점에서 bfs를 진행하며 넓이를 저장해주고 지나간 곳은 0으로 바꾸자
from collections import deque
n,m = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
cnt = 0
answer = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            cnt += 1
            area = 1
            q = deque()
            q.append([i,j])
            array[i][j] = 0
            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<n and 0<=ny<m and array[nx][ny] == 1:
                        array[nx][ny] = 0
                        area += 1
                        q.append([nx,ny])
            answer = max(answer,area)
print(cnt)
print(answer)