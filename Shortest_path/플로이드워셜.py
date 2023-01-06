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
#플로이드 워셜 알고리즘
#아이디어: D(a,b)=min(D(a,k),D(k,b)) 가능한 모든 a,b,k 에 대해서 => O(N^3)의 시간복잡도

INF=987654321

#노드의 개수와 간선의 개수 입력받기
n=int(input())
m=int(input())

#2차원 리스트에 각각의 노드별 거리 저장
graph=[[INF]*(n+1) for _ in range(n+1)] #무한으로 초기화

#자기 자신에게 가는 간선은 0으로 초기화
for i in range(1,n+1):
    graph[i][i]=0

#간선 정보 입력받기
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c
    
#플로이드 워셜 알고리즘

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for a in range(1,n+1):
    for i in range(1,n+1):
        #결과가 INF일 경우 INFINITY 출력하기
        if graph[a][i]==INF:
            print('INFINITY')
        else:
            print(graph[a][i],end=' ')
    print('')#뛰어쓰기 용
# -


