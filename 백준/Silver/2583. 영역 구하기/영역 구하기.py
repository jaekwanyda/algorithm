import sys
input = sys.stdin.readline
#아이디어: 전형적인 bfs 문제
from collections import deque
#m,n,k 입력받기
m,n,k = map(int,input().split())
#가능한 여부를 담은 array 만들어주기
array = [[1 for _ in range(n)]for _ in range(m)]
visited = [[0 for _ in range(n)]for _ in range(m)]
#직사각형 정보들 입력받기
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            #사각형 내부는 못감
            array[i][j] = 0
answer = []
for i in range(m):
    for j in range(n):
        #사각형이 가능한 지점에서 부터 bfs 처리해주기
        if array[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            cnt = 1
            q = deque()
            q.append((i,j))
            while q:
                x,y = q.pop()
                dx = [-1,0,1,0]
                dy = [0,-1,0,1]
                for direction in range(4):
                    nx = dx[direction] + x
                    ny = dy[direction] + y
                    if 0<=nx<m and 0<=ny<n and array[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        cnt += 1
                        q.append((nx, ny))
            answer.append(cnt)
answer.sort()
print(len(answer))
print(*answer)