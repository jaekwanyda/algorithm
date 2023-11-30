import sys
input = sys.stdin.readline
#아이디어: 궁수가 위치 가능한 모든 경우에 대해 진행해보자
n,m,d = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
from itertools import combinations
from collections import deque
import copy
answer = 0
dx = [0,-1,0]
dy = [-1,0,1]
for combi in combinations(range(m),3): #궁수 3명을 임의의 행에 위치
    count = 0 # 총 죽인 적의 수
    test_array = copy.deepcopy(array)
    while test_array: #한 열씩 없애면서 진행
        target = []
        n = len(test_array)
        for c in combi:
            startx = n-1
            starty = c
            visited = [[0]*m for _ in range(n)]
            visited[startx][starty] = 1
            q = deque()
            q.append([startx,starty,1])
            while q:
                x,y,cnt = q.popleft()
                if test_array[x][y] == 1:
                    target.append([x,y])
                    break
                for k in range(3):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and cnt<d:
                        visited[nx][ny] = 1
                        q.append([nx,ny,cnt+1])
        for tx,ty in target:
            if test_array[tx][ty] == 1:
                count += 1
                test_array[tx][ty] = 0
        test_array.pop()
    answer = max(answer,count)
print(answer)