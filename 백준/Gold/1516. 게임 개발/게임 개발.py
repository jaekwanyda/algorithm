import sys
input = sys.stdin.readline
#아이디어: heapq를 쓰면 간단하게 해결될 것 같다
import heapq
n = int(input())
graph = [[] for _ in range(n)]
indegree = [0]*n
times = [0]*n
for i in range(n):
    a_list = list(map(int,input().split()))
    times[i] = a_list[0]
    pre_list = [a-1 for a in a_list[1:-1]]
    for p in pre_list:
        indegree[i] += 1
        graph[p].append(i)
q = []
result = [0]*n
for i,ind in enumerate(indegree):
    if ind == 0:
        heapq.heappush(q,[times[i],i])
        result[i] = times[i]
while q:
    t,node = heapq.heappop(q)
    for nxt in graph[node]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(q,[t+times[nxt],nxt])
            result[nxt] = t+times[nxt]
for r in result:
    print(r)
    