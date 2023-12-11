import sys
input = sys.stdin.readline
#아이디어: 말 방법을 사용가능한 회수가 중요해 보인다. 이것을 저장하면서 graph를 채워나가자
from collections import deque
k = int(input())
m,n = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
horse = [(-1,-2),(-2,-1),(1,-2),(2,-1),(-1,2),(-2,1),(1,2),(2,1)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0]*m for _ in range(n)]
visited[0][0] = k+1
q = deque()
q.append([0,0,k,0])
while q:
    x,y,cnt,d = q.popleft()
    if x == n-1 and y == m-1:
        print(d)
        break
    #말 이동방법으로 이동
    if cnt:
        for i in range(8):
            nx = x + horse[i][0]
            ny = y + horse[i][1]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 and cnt>visited[nx][ny]:
                visited[nx][ny] = cnt
                q.append([nx,ny,cnt-1,d+1])
    #일반적으로 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 and cnt>=visited[nx][ny]:
            visited[nx][ny] = cnt+1
            q.append([nx,ny,cnt,d+1])
else:
    print(-1)