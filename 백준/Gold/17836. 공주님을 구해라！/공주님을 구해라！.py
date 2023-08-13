import sys
input = sys.stdin.readline
#아이디어: bfs를 돌려서 검을 잡은 경우 그냥 다 뚫고 가도록 한다.
import heapq
#n,m,t 입력받기
n,m,t = map(int,input().split())
#성 정보 입력받기
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True
q = []
heapq.heappush(q,(0,0,0)) # 이동거리 0 와 시작 위치 0,0
dxy = [(1,0),(0,1),(-1,0),(0,-1)]
while q:
    d,x,y = heapq.heappop(q)
    #도착한 경우 거리 출력
    if x==n-1 and y == m-1:
        if d<=t:
            print(d)
        else:
            print('Fail')
        break
    if array[x][y] == 2:#검을 잡았으면 그 곳 부터 (n-1,m-1) 까지의 거리 보내주기
        q.append((d+(n-1-x+m-1-y),n-1,m-1))
    else:
        for i in range(4):
            nx = x + dxy[i][0]
            ny = y + dxy[i][1]
            if 0<=nx<n and 0<=ny<m and array[nx][ny] != 1 and not visited[nx][ny]:
                heapq.heappush(q,(d+1,nx,ny))
                visited[nx][ny] = True
else:
    print('Fail')
