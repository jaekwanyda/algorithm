import sys
input = sys.stdin.readline
#아이디어: 높이를 맞춰주고 높이가 같은데 수가 다르면 같이 높이를 올려주자
#시간 초과 발생: 가장 깊은 높이차이(10000) 일 때 10000*50000정도의 시간 복잡도 예상
#빠르게 접근할 방법이 필요
from collections import deque
#n 입력받기
n = int(input())
#트리 정보 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
height = [0]*(n+1)
height[1] = 1 #시작 높이는 1
#부모노드 저장하기
nodes = [i for i in range(n+1)]
q = deque()
q.append(1)
while q:
    start = q.popleft()
    for end in graph[start]:
        if height[end] == 0:
            height[end] = height[start] + 1
            q.append(end)
            nodes[end] = start
#m 입력받기
m = int(input())
#알고싶은 쌍 입력받기
for _ in range(m):
    a,b = map(int,input().split())
    if height[a] > height[b]:
            for _ in range(height[a]-height[b]):
                a = nodes[a]
    elif height[a] < height[b]:
        for _ in range(height[b]-height[a]):
            b = nodes[b]
    while a != b:
        a = nodes[a]
        b = nodes[b]
    print(a)