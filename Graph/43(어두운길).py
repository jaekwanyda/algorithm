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
#이코테 실전 43
#아이디어: 딱봐도 크루스칼 알고리즘을 이용한 최소 신장 찾기 알고리즘이다.
#집의 수 N과 도로의 수 M입력받기
n,m=map(int,input().split())
#도로 정보 입력받기
data=[]
for i in range(m):
    x,y,distance=map(int,input().split())
    data.append((distance,x,y)) #distance 순으로 정렬해주기 위함
data.sort()
#크루스칼 알고리즘을 위한 서로소 집합 정의
def find_parent(parent,a):
    if parent[a]!=a:
        parent[a]=find_parent(parent,parent[a])
    return parent[a]
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

parent=[0]*n
for i in range(n):
    parent[i]=i #부모 노드는 자기 자신으로 초기화
    
min_cost=0 #가능한 최소 금액
total_cost=0 # 가로등 설치에 총 드는 금액

for i in data:
    dis,x,y=i[0],i[1],i[2] #거리와 위치 정보 입력
    total_cost+=dis
    if find_parent(parent,x)!=find_parent(parent,y):
        union_parent(parent,x,y)
        min_cost+=dis


print(total_cost-min_cost)    
# -


