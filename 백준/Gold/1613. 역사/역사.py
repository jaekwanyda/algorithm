import sys
from collections import deque
input = sys.stdin.readline
#아이디어: 플로이드 워셜로, 앞에 있는 번호에서 뒤로 가는 거리는 -1, 반대로는 1 의 graph를 만들자.
#n,k 입력받기
n,k = map(int,input().split())
#서로의 거리를 저장하는 graph 생성
graph = [[0] * (n + 1) for _ in range(n + 1)]

#관계 입력 받기
for _ in range(k):
    # 앞에서 뒤로가는 걸 1로 설정
    a, b= map(int, input().split())
    graph[a][b] = 1 #a->b 
#플로이드 워셜 진행
for q in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][q] >0 and graph[q][b] > 0:
                graph[a][b] = 1
#s 입력받기
s = int(input())
#알고 싶은 관계 입력받기
for _ in range(s):
    a,b = map(int,input().split())
    if graph[a][b] == 1:
        print(-1)
    elif graph[b][a] == 1:
        print(1)
    else:
        print(0)