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

# +
from collections import deque
def bfs(graph,start,visited):
    #deque를 이용해서 Queue 구현
    queue=deque([start])
    #현재 노드 방문 처리
    visited[start]=True
    #큐가 완전히 다 비워질 때까지 계속
    while queue: #이런 while 문도 가능하다는것 숙지
        v=queue.popleft()
        print(v,end=' ')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들 모드 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                
#인접리스트로 정리(인접행렬과 차이점 숙지하기)
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9
bfs(graph,1,visited)
# -


