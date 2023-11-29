import sys
input = sys.stdin.readline
#아이디어: 최단거리 중 가장 먼 곳 찾기 한번 bfs를 돌려서 마지막에 도착하는 지점에서 다시 bfs를 돌려보자
from collections import deque
n,m = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(input()))
visited = [[0]*m for _ in range(n)]
dx = [0,0,1,-1]
dy = [-1,1,0,0]
answer = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == "L" and not visited[i][j]:
            q = deque()
            q.append([i,j])
            visited[i][j] = 1
            check_list = []
            while q:
                x,y = q.popleft()
                check = False
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<n and 0<=ny<m and array[nx][ny] == 'L' and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        check = True
                        q.append([nx,ny])
                if not check:
                    check_list.append([x,y])
            for lastx,lasty in check_list:
                check_visited = [[0]*m for _ in range(n)]
                check_q = deque()
                check_q.append([lastx,lasty,0])
                check_visited[lastx][lasty] = 1
                while check_q:
                    x,y,cnt = check_q.popleft()
                    answer = max(answer,cnt)
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<n and 0<=ny<m and array[nx][ny] == 'L' and not check_visited[nx][ny]:
                            check_visited[nx][ny] = 1
                            check_q.append([nx,ny,cnt+1])
print(answer)