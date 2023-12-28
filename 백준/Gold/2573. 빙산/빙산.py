import sys
import copy
from collections import deque
input = sys.stdin.readline
#아이디어: bfs
n,m = map(int,input().split())
ice = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    ice.append(list(map(int,input().split())))
year = 0
melt = [[0]*m for _ in range(n)]
for i in range(n):
        for j in range(m):
            if ice[i][j] == 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<m:
                        melt[nx][ny] += 1
while sum(sum(b) for b in ice) != 0:
    year += 1
    new_ice = copy.deepcopy(ice)
    #얼음 녹여주기
    new_sea = []
    for i in range(n):
        for j in range(m):
            if new_ice[i][j] > 0:
                new_ice[i][j] -= melt[i][j]
                if new_ice[i][j] <= 0:
                    new_ice[i][j] =0
                    new_sea.append((i,j))
    for x,y in new_sea:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                melt[nx][ny] += 1
    #얼음 덩어리 개수 세주기
    ice = copy.deepcopy(new_ice)
    cnt = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            if new_ice[i][j] > 0:
                new_ice[i][j] = 0
                cnt += 1
                q.append((i,j))
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<n and 0<=ny<m and new_ice[nx][ny] > 0:
                            new_ice[nx][ny] = 0
                            q.append((nx,ny))
    if cnt > 1:
        print(year)
        break
else:
    print(0)
                        