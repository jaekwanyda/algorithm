import sys
input = sys.stdin.readline
#아이디어: bfs를 구현해 각 점 별로 4개까지 경로를 모두 찾아준다. 시간 단축을 위해 이미 bfs를 진행한 점은 방문하지 않도록 하자
from collections import deque
#input n,m
n,m = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
# visited = {}
q = deque()
answer = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for i in range(n):
    for j in range(m):
        # visited[i][j] = 1
        q.append((i,j,1,array[i][j],[(i,j)])) #x,y 좌표와 이동한 칸 수, 총 합, 이동 정보
        while q:
            x,y,d,total,d_list = q.pop()
            if d == 3:
                if all(px == x for px,_ in d_list): #이전까지 이동이 전부 한 수평선 위면 ㅗ,ㅜ 모양 체크해주기
                    if x>0:
                        answer = max(answer,total+array[x-1][d_list[1][1]])
                    if x<n-1:
                        answer = max(answer,total+array[x+1][d_list[1][1]])
                elif all(py == y for _,py in d_list): #마찬가지로 수직선인 경우
                    if y>0:
                        answer = max(answer,total+array[d_list[1][0]][y-1])
                    if y<m-1:
                        answer = max(answer,total+array[d_list[1][0]][y+1])            
            if d == 4:  
                answer = max(answer,total)            
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in d_list:
                    q.append((nx,ny,d+1,total+array[nx][ny],d_list+[(nx,ny)]))
print(answer)
            