import sys
input = sys.stdin.readline
#아이디어: 열쇠를 먹었을 때 먹은 열쇠의 종류의 새로운 visied를 이용하면 될 것 같다.
from collections import deque
#n,m 입력받기
n,m = map(int,input().split())
#미로 정보 입력받기
graph = [input() for _ in range(n)]
#시작 정보 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            startx, starty = i,j
            break
#열쇠를 먹은 경우에 따라 총 64 가지 경우의 visited 만들어주기
visited = [[[0]*m for _ in range(n)] for _ in range(2**6)]
q = deque()
q.append((startx,starty,0,0)) #시작 위치 x,y와 열쇠정보 0,이동거리 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]
possi = False
while q:
    x,y,key,d = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[key][nx][ny] and graph[nx][ny] != '#':
            #만약 문이 있고 문에 해당되는 key가 있으면 deque에 넣어주기
            if graph[nx][ny].isupper() and 2**(ord(str.lower(graph[nx][ny]))-97) & key != 0:
                q.append((nx,ny,key, d+1))
                visited[key][nx][ny] = True
                continue
            #key가 있는 칸이면 key를 먹고 visited 바꿔주기
            if graph[nx][ny].islower():
                q.append((nx,ny,key|2**(ord(graph[nx][ny])-97),d+1))
                visited[key][nx][ny] = True
            #달이 있는 칸이면 정답 등록
            if graph[nx][ny] == '1':
                answer = d+1
                possi = True
                break
            if graph[nx][ny] == '.' or graph[nx][ny] == '0':
                q.append((nx,ny,key,d+1))
                visited[key][nx][ny] = True
    #만약 정답이 나왔다면 while 구문 멈추기
    if possi:
        break
if possi:
    print(answer)
else:
    print(-1)
