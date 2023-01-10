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
#이코테 실전 37(백준 11404)
#아이디어: 모든 도시에 대해 구하니까 플로이드 워셜을 쓰면 해결 가능할 것 같다.
#도시 개수 n 입력받기
n=int(input())
INF=987654321
graph=[[INF]*(n+1) for _ in range(n+1)] #각각의 거리가 INF인 2차원 행렬 생성
for i in range(1,n+1):
    graph[i][i]=0 #자기 자신까지 거리는 0으로 초기화
#버스 개수 m 입력 받기
m=int(input())
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=min(graph[a][b],c) #만약 버스 노선이 겹치면 더 작은 값으로 해주기 위함

#플로이드 워셜 사용
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
            
#거리 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print(0)
        else:
            print(graph[i][j],end=' ')
            
    print('')
# -


