import sys
input = sys.stdin.readline
#아이디어: bfs
from collections import deque
s = int(input())
array = [[0 for _ in range(2*s+1)] for _ in range(2*s+1)]
q = deque()
q.append([1, 0, 0])
while q:
    screen, clip, t = q.popleft()
    if screen == s:
        print(t)
        break
    if array[screen][clip]:
        continue
    array[screen][clip] = 1
    if 1 <=screen and screen < 2*s+1:
        q.append([screen-1, clip, t+1])
        q.append([screen, screen, t+1])
    if clip and screen+clip < 2*s+1:
        q.append([screen+clip, clip, t+1])