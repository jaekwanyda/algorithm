from collections import deque
#n,m 입력받기
n,m = map(int,input().split())
#Ai,Bi 입력받기
graph=[[] for _ in range(n+1)]
for _ in range(m):
    ai,bi = map(int,input().split())
    graph[ai] += [bi]
    graph[bi] += [ai]
distance = [0]*(n+1)
visited = [False]*(n+1)
q = deque()
q.append((1,0)) #시작노드 1과 거리 0 을 먼저 넣는다
visited[1] = True
#bfs 돌리기
while q:
    node, d = q.popleft()
    for n_node in graph[node]:
        if not visited[n_node]:
            #아직 방문하지 않은 노드인 경우 q에 추가
            q.append((n_node,d+1))
            visited[n_node] = True
            distance[n_node] = d+1
m = max(distance)
hide_node = n+1; number = 0
for i,j in enumerate(distance):
    if j==m:
        if hide_node>i:
            hide_node = i
        number += 1
print(hide_node,m,number)