import sys
input = sys.stdin.readline
#아이디어: 다익스트라
import heapq
INF = float('inf')
v,e = map(int,input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)
for _ in range(e):
    u,_v,w = map(int,input().split())
    graph[u].append((_v,w))
q= []
heapq.heappush(q,(0,start))
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost =dist+ i[1]
        if cost < distance[i[0]] :
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))
for i in range(1,v+1):
    if distance[i] == float('inf'):
        print("INF")
    else:
        print(distance[i])