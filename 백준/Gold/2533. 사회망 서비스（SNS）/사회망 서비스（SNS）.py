import sys
input = sys.stdin.readline
#아이디어: dp를 이용하면 가능할 것 같다.
sys.setrecursionlimit(10**6)
from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
q = deque()
q.append(1)
child_list = [[] for _ in range(n+1)]
while q:
    node = q.popleft()
    for nxt_node in graph[node]:
        if not child_list[nxt_node]:
            q.append(nxt_node)
            child_list[node].append(nxt_node)
result = [0]*(n+1)
def recursion(node):
    if not child_list[node]:
        return 0
    change = 1 #자신이 변해야 하므로
    not_change = 0
    for child in child_list[node]:
        #node가 변하는 경우 => 자식들은 변해도 되고 안변해도 된다.(자식이 없다면 무조건 안변해도 된다)
        if result[child]:
            change += result[child]
        else:
            change += recursion(child)
        #node가 안변하는 경우 => 자식들은 무조건 변해야 한다.
        not_change += 1
        for c in child_list[child]:
            if result[c]:
                not_change += result[c]
            else:
                not_change += recursion(c)
    result[node] = min(change,not_change)
    return result[node]
print(recursion(1))