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
#DFS는 스택을 이용한 깊이 우선 탐색 알고리즘이다.
#스택은 리스트로 구현이 쉽기 때문에 이와 같이도 구현 가능하다.
def dfs(graph,v,visited):
    #현재 노드를 방문 처리
    visited[v]=True
    print(v,end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적을로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

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
dfs(graph,1,visited)
# -


