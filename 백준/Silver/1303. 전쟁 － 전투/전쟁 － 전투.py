import sys
from collections import deque
input = sys.stdin.readline
#아이디어: 둘 다 BFS 돌리기!=> answer에 bfs가 진행될 때 마다 1씩 더해주고 끝나면 0으로 초기화!
dx = [0,-1,0,1]
dy = [-1,0,1,0]
def bfs(p,w,a):
    q = deque()
    q.append((p,w))
    visited[w][p] = 1
    result = 1
    while q:
        x,y = q.popleft()
        for o in range(4):
            nx = dx[o] + x
            ny = dy[o] + y
            if nx >= 0 and nx < n and ny >=0 and ny <m:
                if not visited[ny][nx] and array[ny][nx] == a:
                    visited[ny][nx] = 1
                    result += 1
                    q.append((nx,ny))
    return result
#n,m 입력 받기
n,m = map(int,input().split())
#array 입력받기
array = [list(input()) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
#blue 합과 white 합
blue_sum = 0
white_sum = 0

for i in range(n):
    for j in range(m):
        if not visited[j][i]:
            k = bfs(i,j,array[j][i])
            if array[j][i] == 'W':
                white_sum += k**2
            elif array[j][i] == 'B':
                blue_sum += k**2
print(white_sum, blue_sum)
