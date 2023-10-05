import sys
input = sys.stdin.readline
#아이디어: bfs문제같다
from collections import deque
#input n,k
n,k = map(int,input().split())
visited = [0]*(100001)
visited[n] = 1
q = deque()
q.append((n,0))
while q:
    x,d = q.popleft()
    if x == k:
        print(d)
        break
    if x >= 1 and not visited[x-1]:
        q.append((x-1,d+1))
        visited[x-1] = 1
    if x<100000 and not visited[x+1]:
        q.append((x+1,d+1))
        visited[x+1] = 1
    if x <= 50000 and not visited[x*2]:
        q.append((2*x,d+1))
        visited[2*x] = 1