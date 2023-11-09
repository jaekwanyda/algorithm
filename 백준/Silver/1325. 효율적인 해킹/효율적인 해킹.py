import sys
input = sys.stdin.readline
#아이디어: dfs를 하며 visited로 방문 처리하며 해결해보자
from collections import deque
n,m = map(int,input().split())
answer = [0]*n
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split()) #b가 a의 부모
    a,b = a-1,b-1
    graph[b].append(a) #b를 해킹하면 a는 보너스
def bfs(node):
    q = deque()
    q.append(node)
    visited = [0]*n
    visited[node] = 1
    cnt = 0
    while q:
        x = q.popleft()
        cnt += 1
        for g in graph[x]:
            if not visited[g]:
                visited[g] = 1
                q.append(g)
    return cnt     
for i in range(n):
    answer[i] = bfs(i)
target = max(answer)
result = []
for i,a in enumerate(answer):    
    if a == target:
        result.append(i+1)
print(*result)