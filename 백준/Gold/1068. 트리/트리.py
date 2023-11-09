import sys
input = sys.stdin.readline
#아이디어: 짜르고 이어진 것들 indegree -1로 바꾸고 마지막에 indegree가 0인 것 개수 세보자
n = int(input())
parents = list(map(int,input().split()))
indegree = [0]*(n)
graph = [[] for _ in range(n)] #자식 노드 정보
for node,parent in enumerate(parents):
    if parent != -1:
        graph[parent].append(node)
        indegree[parent] += 1
cut_node = int(input())
indegree[parents[cut_node]] -= 1
def cut(cut_node):
    indegree[cut_node] = -1
    for node in graph[cut_node]:
        cut(node)
cut(cut_node)
print(sum(cnt==0 for cnt in indegree))