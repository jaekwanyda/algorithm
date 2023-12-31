import sys
import copy
import heapq
input = sys.stdin.readline
#아이디어: 다익스트라
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    start,end,cost = map(int,input().split())
    graph[start].append((end,cost))
result_start, result_end = map(int,input().split())
q = []
heapq.heappush(q,(0,result_start))
while q:
    cost, node = heapq.heappop(q)
    if node == result_end:
        print(cost)
        break
    if visited[node]:
        continue
    visited[node] = True
    for next_node, add_cost in graph[node]:
        heapq.heappush(q,(cost+add_cost,next_node))
