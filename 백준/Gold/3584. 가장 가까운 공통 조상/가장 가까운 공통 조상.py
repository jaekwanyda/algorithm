import sys
input = sys.stdin.readline
#아이디어: 루트로 가는 경로 보고 겹치는 것 중 가장 빨리 나오는 것 출력
#t 입력 받기
t = int(input())
for _ in range(t):
    #n 입력받기
    n = int(input())
    #간선 입력받을 list
    graph = [0 for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[b] = a #b의 부모는 a이다
    #정답을 찾아야할 것
    x, y =map(int,input().split())
    x_to_parent = set()
    while True:
        if x == 0:
            break
        x_to_parent.add(x)
        x = graph[x]
    while True:
       if y in x_to_parent:
           print(y)
           break
       y = graph[y] 