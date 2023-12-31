import sys
import copy
from collections import deque
input = sys.stdin.readline
#아이디어: bfs
t = int(input())
dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]
for _ in range(t):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    startx, starty = map(int,input().split())
    endx, endy = map(int,input().split())
    q = deque()
    q.append((startx,starty))
    while q:
        x,y = q.popleft()
        if x == endx and y == endy:
            print(graph[x][y])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not graph[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
