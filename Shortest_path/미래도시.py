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
#이코테 최단 경로 연습 2
#아이디어: 총 100개의 노드가 주어지므로 플로이드 워셜 사용하기
#의문: 만약 K-N 순서로 방문해야 하는데 최단거리 조건이 N을 거쳐갔을 때라면 어떻게 처리할지
#일단 그런 경우에 대해서 명시되어 있지 않으니 플로이드로 해본다.
#전체 회사의 수 N과 경로 수 M입력받기
n,m=map(int,input().split())

INF=987654321

#2차원 리스트에 각각의 노드별 거리 저장
graph=[[INF]*(n+1) for _ in range(n+1)] #무한으로 초기화

#자기 자신에게 가는 간선은 0으로 초기화
for i in range(1,n+1):
    graph[i][i]=0
    
#간선 정보 입력받기
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

#플로이드 워셜 알고리즘

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

            
#X와 K입력받기
x,k=map(int,input().split())

result=graph[1][k]+graph[k][x]
if result>=INF:
    print(-1)
else:
    print(result)
# -


