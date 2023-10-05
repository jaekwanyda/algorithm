import sys
input = sys.stdin.readline
#아이디어: 그냥 DFS, BFS 구현해보자
from collections import deque
stack = []
q = deque()
#n,m,v 입력받기
n,m,v = map(int,input().split())
#간선 정보 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#방문 처리해주기
visited_s = []
visited_q = []
stack.append(v)
q.append(v)
#dfs
while stack:
    nv = stack.pop()
    if not nv in visited_s:
        visited_s.append(nv)
        for i in sorted(graph[nv],key= lambda x:-x):
            if not i in visited_s:
                stack.append(i)
print(*visited_s)
#bfs
while q:
    nv = q.popleft()
    if not nv in visited_q:
        visited_q.append(nv)
        for i in sorted(graph[nv]):
            if not i in visited_q:
                q.append(i)
print(*visited_q)