import sys
input = sys.stdin.readline
#아이디어: ㄷ이 발생되는 경우(양쪽 노드가 2개 이상의 인접노드를 가질 때), ㅈ이 발생되는 경우(한 노드의 인접 노드가 3 이상일 때)를 세주자
import math
#n 입력받기
n = int(input())
#트리 정보 입력받기
graph = []
#인접노드 개수 저장
degree = [0]*(n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    graph.append((a,b))
    degree[a] += 1
    degree[b] += 1
d = 0
g = 0
#각 간선별로 ㄷ자 가능한지 확인
for s,e in graph:
    d += (degree[s]-1)*(degree[e]-1)
#각 노드별로 ㅈ자 가능한지 확인
for i in range(1,n+1):
    if degree[i] >= 3:
        g += math.comb(degree[i],3)
if d > g*3:
    print('D')
elif d < g*3:
    print('G')
else:
    print('DUDUDUNGA')