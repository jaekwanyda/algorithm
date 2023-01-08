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
#이코테 기출 15
#아이디어: 최단거리가 K인 모든 지점을 구하란 문제로 BFS를 쓸 것을 예상해 볼 수 있다.
from collections import deque
#도시의 개수 N, 간선의 개수 M, 원하는 거리 K, 출발 도시의 번호 X 입력받기
n,m,k,start=map(int,input().split())

#간선 정보 입력받기
graph=[[] for _ in range(n+1)] #도시별 간선 정보
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
#방문 여부 확인하기
visited=[False]*(n+1) #중간 생각: 공간복잡도 걱정이 되긴 했지만 메모리 제한이 256MB라서 일단은 진행했다.
#시작지점 방문처리하고 큐에 추가
q=deque()
visited[start]=True
q.append(start)
distance=[0]*(n+1)

while q: #중간 생각.여기도 시간복잡도 걱정이 되었다. 만약 시간이 초과하면 k+1 번째까지만 진행하는 등의 방법을 생각해야 할 것같다.
    now=q.popleft()
    for i in graph[now]:#연결된 도시에 인해서만 진행
        if not visited[i]: #방문 안했을 경우만 추가로 진행
            distance[i]=distance[now]+1
            visited[i]=True
            q.append(i)

for i in range(1,n+1):
    if distance[i]==k: #최단거리가 k일 때만 출력
        print(i,end='')
# -


