import sys
input = sys.stdin.readline
#아이디어: 단순하게 정수가 입력된 정점을 찾고 그 정점에서 0이 될떄까지 올라가자
#n,k 입력받기
n,k = map(int,input().split())
#간선 정보 입력받기
graph = [0]*n
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[b] = a
#정점에 부여된 값 입력받기
nodes = list(map(int,input().split()))
#찾는 노드의 index
target = nodes.index(k)
#0이 나올때 까지 올라가기
cnt = 0
while target != 0:
    target = graph[target]
    cnt += 1
print(cnt)