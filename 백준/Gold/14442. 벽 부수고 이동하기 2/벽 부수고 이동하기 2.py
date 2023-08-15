import sys
input = sys.stdin.readline
#아이디어: bfs로 풀어보자
from collections import deque
#n,m,k 입력받기
n,m,k = map(int,input().split())
#맵 정보 입력받기
array = []
for _ in range(n):
    array.append(list(map(int,input().strip())))
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(11)]
for i in range(11):
    visited[i][0][0] = True
q = deque()
q.append((0,0,k,1)) #시작 위치와 뿌시기 가능한 횟수 k, 이동 거리 1 입력
answer = -1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while q:
    x,y,t,d = q.popleft()
    if x == n-1 and y == m-1:
        answer = d
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if array[nx][ny] == 1 and t > 0 and not visited[t-1][nx][ny]:
                visited[t-1][nx][ny] = True
                q.append((nx,ny,t-1,d+1))
            elif array[nx][ny] == 0 and not visited[t][nx][ny]:
                visited[t][nx][ny] = True
                q.append((nx,ny,t,d+1))
print(answer)
