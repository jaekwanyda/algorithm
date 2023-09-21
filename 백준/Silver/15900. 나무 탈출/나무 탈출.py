import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
#아이디어: 리프 노드에서 루트 노드까지의 거리를 전부 계산해서 홀수면 이긴다.
#정점 개수 입력받기
n = int(input())
#간선 정보 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = 0
stack = []
for node in graph[1]:
    stack.append((1,node,1))
while stack:
    prenode,node,cnt = stack.pop()
    if len(graph[node]) == 1:
        answer += cnt
        continue
    for next_node in graph[node]:
        if next_node == prenode:
            continue
        stack.append((node,next_node,cnt+1))
if answer % 2 == 1:
    print('Yes')
else:
    print('No')