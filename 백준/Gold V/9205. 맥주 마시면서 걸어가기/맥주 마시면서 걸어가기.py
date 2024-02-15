import sys
input = sys.stdin.readline
#아이디어: bfs
from collections import deque
for _ in range(int(input())):
    n = int(input())
    start_x, start_y = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(n)]
    target_x, target_y = map(int, input().split())
    q = deque([(start_x, start_y)])
    visited = set()
    while q:
        x, y = q.popleft()
        if abs(target_x-x) + abs(target_y-y) <= 1000:
            print('happy')
            break
        for i in range(n):
            store_x, store_y = store[i]
            if (store_x, store_y) not in visited and abs(store_x-x) + abs(store_y-y) <= 1000:
                visited.add((store_x, store_y))
                q.append((store_x, store_y))
    else:
        print('sad')