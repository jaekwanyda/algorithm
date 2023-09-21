import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
#아이디어: bfs로 탐색해서 f층 중 갈 수 있는 모든 층을 찾아보자.
from collections import deque
#엘레베이터 정보 입력받기
f,s,g,u,d = map(int,input().split())
visited = [False]*(f+1)
q = deque()
q.append((s,0))
visited[s] = True
answer = -1
while q:
    floor,cnt = q.popleft()
    if floor == g:
        answer = cnt
        break
    if floor + u <= f and not visited[floor + u]:
        q.append((floor+u,cnt+1))
        visited[floor + u] = True
    if floor - d > 0 and not visited[floor -d]:
        q.append((floor-d,cnt+1))
        visited[floor - d] = True
if answer == -1:
    print('use the stairs')
else:
    print(answer)