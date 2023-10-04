import sys
input = sys.stdin.readline
#아이디어: 섬의 개수와 문제가 동일하다
from collections import deque
#t 입력받기
t = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for _ in range(t):
    #m,n,k 입력받기
    m,n,k = map(int,input().split())
    #배추밭 정보 입력받기
    array = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        array[y][x] = 1
    q = deque()
    answer = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1:
                q.append((i,j))
                array[i][j] = 0
                answer += 1
            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<n and 0<=ny<m and array[nx][ny] == 1:
                        q.append((nx,ny))
                        array[nx][ny] = 0
    print(answer)