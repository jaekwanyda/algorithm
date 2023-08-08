import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
q = []

for i in range(n):
    for j in range(n):
        heapq.heappush(q, (array[i][j], i, j))

visit = [[0] * n for _ in range(n)]  # Using 'visit' array for memoization
answer = 0

def dfs(x, y):
    if visit[x][y] != 0:
        return visit[x][y]
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    max_length = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and array[x][y] < array[nx][ny]:
            max_length = max(max_length, dfs(nx, ny) + 1)
    
    visit[x][y] = max_length  # Memoize the result
    return max_length

while q:
    _, x, y = heapq.heappop(q)
    answer = max(answer, dfs(x, y))

print(answer)
