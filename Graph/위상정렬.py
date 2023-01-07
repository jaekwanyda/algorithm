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
#위상정렬은 방향그래프의 모든 노드를 순서에 거슬리지 않게 나열하는 것이다
#이때 사이클이 존재하는지도 확인할 수 있다.
from collections import deque
#노드의 개수와 간선의 개수 입력받기
v,e=map(int,input().split())
#모든 노드에 대한 진입차수는 0으로 초기화
indegree=[0]*(v+1)
#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph=[[] for _ in range(v+1)]

#간선 정보 입력받기
for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    #진입차수 증가시키기
    indegree[b]+=1
    
#위상 정렬 함수

def topology_sort():
    result=[] #정렬된 결과를 담을 리스트
    q=deque()
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    while q: #q가 빌때까지
        a=q.popleft()
        result.append(a)
        for i in graph[a]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in result:
        print(i,end=' ')

    
topology_sort()

# -


