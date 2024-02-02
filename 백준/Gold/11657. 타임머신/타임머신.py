import sys
input = sys.stdin.readline
#아이디어: 밸만포드
n, m = map(int, input().split()) 
edges = [] 
distance = [float('inf')] * (n+1) 
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
possi = True
distance[1] = 0 
for i in range(n): 
    for j in range(m): 
        node, nxt_node, cost = edges[j] 
        if distance[node] != float('inf') and distance[nxt_node] > distance[node] + cost:
            distance[nxt_node] = distance[node] + cost
            if i == n-1:
                possi = False
if possi:
    for i in range(2, n+1):
        if distance[i] == float('inf'): 
            print('-1')
        else:
            print(distance[i])
else:
    print('-1')