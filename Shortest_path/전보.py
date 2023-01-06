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
#이코테 최단 경로 연습 3
#아이디어: C에서 연결된 곳들과 그 중 가장 먼곳 출력하기. 개수가 많고, C에서 연결된 것만 보면 되니까 다익스트라 사용

#도시의 갯수 N 통로의 개수 M 메세지를 보내고 싶은 도시 C 입력
n,m,start=map(int,input().split())

INF=987654321
distance=[INF]*(n+1)

#입력받는 간선 정보 저장할 리스트 생성
graph=[[] for i in range(n+1)] 
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    
import heapq

#다익스트라 알고리즘 구현 까먹음 다시 공부하기

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) #시작지점은 거리 0
    distance[start]=0
    while q: #q가 빌때까지
        dist,now=heapq.heappop(q) #heapq 문법 잘보기
        if distance[now]<dist:#이미 처리됐다면 넘어가기
            continue
        for i in graph[now]:
            cost=dist+i[1] #자신을 거쳐 지나갔을 때 비용
            if cost<distance[i[0]]: #만약 자기를 지나갔을 때가 더 빠르면 업데이트
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0])) #업데이트 했을 경우 큐로 최단거리 정보 넘겨주기

dijkstra(start)

sum=0
max_dis=0
for d in distance:
    if d!=INF:
        sum+=1
        max_dis=max(max_dis,d)

print(sum-1,max_dis)
# -




