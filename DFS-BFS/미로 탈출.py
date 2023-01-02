# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

#아이디어: 가장 가까운 노드부터 탐색하는 BFS를 이용해서 최단 거리를 찾아보자
#N,M 입력
n,m=map(int,input().split())
#미로 입력(괴물이 있는부분이 0)
array=[list(map(int,input().split())) for _ in range(n)]
from collections import deque
#상하좌우 이동 정의
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    #큐가 완전히 빌 때까지 반복
    while queue:
        x,y=queue.popleft()
        #이 문제는 그래프로 보자면 각 지점별로 상하좌우 최대 4가지의 이동이 가능한 정점들이다.
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #괴물이 있을 경우나 그래프 밖일 경우 가지 않는다.
            if nx<0 or ny<0 or nx>=n or ny>=m: #제일 큰 오류를 먼저 제거해준다. list index에서 벗어나면 아예 계산이 안되기 때문!!(틀림)
                continue
            if array[nx][ny]==0 :
                continue
            #처음 방문한 경우일 때만 추가한다.
            if array[nx][ny]==1:
                array[nx][ny]=array[x][y]+1
                queue.append((nx,ny))
    return array[n-1][m-1]
print(bfs(0,0))


