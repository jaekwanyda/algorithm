import sys
input = sys.stdin.readline
#아이디어:경계 중 가장 작은 수를 최대 높이로 지정할 수 있다.
#이때 이 수가 자기보다 작으면 채우지 않으면 된다
from collections import deque
#n,m 입력받기
n,m = map(int,input().split())
#array 입력받기
array = [list(map(int,input().rstrip())) for _ in range(n)]
#어차피 외각은 무조건 불가능하므로 (1,1) 부터 (n-2,m-2) 까지 bfs를 진행해주자
visited = [[False]*m for _ in range(n)]
dx = [0,-1,0,1] #왼쪽부터 시계방향
dy = [-1,0,1,0]
answer = 0
def bfs(x,y):
    global answer
    q = deque()
    q.append((x,y))
    me = array[x][y]
    visited[x][y] = 1
    lim = 100 #경계 중 가장 작은 수 저장하기
    visit_set = {(x,y)} #방문한 노드들 list 
    poss = True #수영장이 가능한지 여부
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #자기보다 작거나 같은 경우 이동 가능, 대신 외각인 경우 수영장 불가능
            if array[nx][ny] <= me:
                if nx == 0 or nx == n-1 or ny == 0 or ny == m-1:
                    poss = False
                else:
                    #이미 이번 bfs에서 방문하지 않은 경우만 방문
                    if not (nx, ny) in visit_set:
                        visit_set.add((nx,ny))
                        q.append((nx,ny))
            #큰 경우는 경계로 저장하기 그 중 가장 작은 값을 lim으로 저장
            else:
                lim = min(lim,array[nx][ny])
    #수영장 만들기가 가능하면
    if poss:
        for kx, ky in visit_set:
            answer += lim - array[kx][ky]
            visited[kx][ky] = 1
            array[kx][ky] = lim
    
#방문하지 않은 지점에서만 bfs를 진행
for i in range(1,n-1):
    for j in range(1,m-1):
        if not visited[i][j]:
            bfs(i,j)
print(answer)