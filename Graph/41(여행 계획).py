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
#이코테 실전 41
#아이디어: 서로소 집합을 이용해 입력된 도시들이 한 집합안에 속하면 여행 가능.
#여행지 수 n 과 여행 계획에 속한 도시의 수 m
n,m=map(int,input().split())
#여행지 연결 정보 입력받기
data=[list(map(int,input().split())) for _ in range(n)]
#find, union 정의하기

def find_parent(parent,a):
    if parent[a]!=a:
        parent[a]=find_parent(parent,parent[a])
    return parent[a]
        
def union_parent(parent,a,b):
    x=find_parent(parent,a)
    y=find_parent(parent,b)
    
    if x<y:
        parent[b]=a
    else:
        parent[a]=b
        
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i #부모 노드는 자기 자신으로 초기화
#여행지 연결 정보를 통해 union 진행하기
for i in range(n):
    for j in range(n):
        if data[i][j]==1: #연결되었을 때 union 진행
            union_parent(parent,i+1,j+1) #입력을 index 0 부터 받아 1 차이남

#여행 계획 리스트 받기
travel=list(map(int,input().split()))

#여행 계획 확인하기
a=find_parent(parent,travel[0]) #첫번째 여행지의 부모노드와 모두가 같으면 여행이 가능하다.
s=0 #맞는 수
for i in travel:
    b=find_parent(parent,i)
    if a==b:
        s+=1

if s==len(travel):
    print('Yes')
else:
    print('No')
# -


