# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
#이코테 연습
#import sys
#input = sys.stdin.readline #더 빠르게 입력 받는 방법
Inf=987654321

n,m=map(int,input().split())
start=int(input())#시작 번호 입력
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph=[[] for i in range(n+1)]
#방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited=[False]*(n+1)
#최단 거리 테이블을 모두 무한으로 초기화
distance=[Inf]*(n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) #간선 정보 추가해주는 방법
    
#방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value=Inf
    index=0
    for i in range(1,n+1): #노드별로 확인 (선형시간)
        if distance[i]<min_value and visited[i]==False:
            min_value=distance[i]
            index=i
    return index

#다익스트라 알고리즘
def dijkstra(start):
    #시작 노드 초기화
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1] #등록되어 있는 간선 별로 거리 등록
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now=get_smallest_node()
        visited[now]=True
        #현재 노드와 연결된것들을 확인해서 업데이트 필요시 업데이트
        for j in graph[now]:
            #자기를 거쳐갔을 때의 비용
            cost=distance[now]+j[1]
            if distance[j[0]]>cost:
                 distance[j[0]]=j[1]
                    
dijkstra(start)

for i in range(1,n+1):
    #도달할 수 없는 경우 , 무한(INFINITY) 출력
    if distance[i]==Inf:
        print("INFINITY")
    else:
        print(distance[i])

# +
#개선된 다익스트라
import heapq
INF=987654321
n,m=map(int,input().split())
start=int(input())#시작 번호 입력
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph=[[] for i in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance=[Inf]*(n+1)
#모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) #간선 정보 추가해주는 방법

def dijkstra(start):
    q=[]
    #시작노드로 가는 최단경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue 
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

for i in range(1,n+1):
    #도달할 수 없는 경우 , 무한(INFINITY) 출력
    if distance[i]==Inf:
        print("INFINITY")
    else:
        print(distance[i])
