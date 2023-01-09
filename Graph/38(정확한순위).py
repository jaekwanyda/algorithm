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
#이코테 실전 38
#아이디어: 각각에 대해서 플로이드를 쓴 후 전부 연결되어 있다면 순위를 알 수 있다.
n,m=map(int,input().split())
INF=987654321
graph=[[INF]*(n+1) for _ in range(n+1)] #각각의 거리가 INF인 2차원 행렬 생성
for i in range(1,n+1):
    graph[i][i]=0 #자기 자신까지 거리는 0으로 초기화
#성적 정보 입력받기
for i in range(m):
    a,b=map(int,input().split()) #a학생이 b학생보다 성적이 낮다=> a->b로 연결된 방향 그래프로 적용
    graph[a][b]=1 
    
#플로이드 워셜 사용
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

#순위를 알 수 있는 학생 수 출력하기
students=0
for i in range(1,n+1):
    c=0 #연결된 수
    for j in range(1,n+1):
        if graph[i][j]!=INF or graph[j][i]!=INF:
            c+=1
    if c==n:
        students+=1
print(students)
# -


