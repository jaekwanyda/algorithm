import sys
input = sys.stdin.readline
#아이디어: 그냥 크루스칼 알고리즘
v, e = map(int, input().split())
edges = []
for _ in range(e):
    a,b,c = map(int, input().split())
    edges.append((a, b, c))
edges.sort(key=lambda x: x[2])
parents = [i for i in range(v+1)]
def parent(x):
    if parents[x] == x:
        return x
    parents[x] = parent(parents[x])
    return parents[x]
def union(a, b):
    a = parent(a)
    b = parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b        
def same_parent(a, b):
    return parent(a) == parent(b)
answer = 0
for a, b, cost in edges:
    if not same_parent(a, b):
        union(a, b)
        answer += cost
print(answer)