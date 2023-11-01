import sys
input = sys.stdin.readline
#아이디어: 모든 경우의 수 확인해주기
n,m = map(int,input().split())
from itertools import combinations
from collections import deque
import copy
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
#바이러스 위치 찾기
virus = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 2:
            array[i][j] = -1
            virus.append((i,j))
answer = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for comb in combinations(virus,m):
    copy_array = copy.deepcopy(array)
    q = deque()
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for c in comb:
        q.append((c[0],c[1],0)) #x,y 좌표와 시작 시간
        visited[c[0]][c[1]] = True
    while q:
        x,y,cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if copy_array[nx][ny] == 0:
                    copy_array[nx][ny] = cnt+1
                    q.append((nx,ny,cnt+1))
                elif copy_array[nx][ny] == -1:
                    q.append((nx,ny,cnt+1))
                visited[nx][ny] = True
    if all(all((a!=0) for a in arr) for arr in copy_array):
        answer.append(max(max(c) for c in copy_array))
if all(all(a==1 or a==-1 for a in arr) for arr in array):
    print(0)
elif answer:
    print(min(answer))
else:
    print(-1)