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
#크루스칼 알고리즘: 간선 비용대로 오름차순후 가장 낮은 비용의 간선부터 차례대로 추가. 만약 이어져 있다면 추가 X
#이어짐 여부를 union과 find를 통해서 알 수 있다.
#특정 원소가 속한 집합 찾기(경로 압축)
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
v,e=map(int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i # 부모를 자기 자신으로 초기화
import heapq
q=[]
for _ in range(e):
    a,b,cost=map(int,input().split())
    heapq.heappush(q,(cost,a,b)) #오름차순을 cost 기준으로 하기 위해 제일 앞에 둠
#총 거리 계산
result=0
while q: #q가 다 빌때까지
    cost,a,b=heapq.heappop(q)
    #사이클이 발생하지 않을 때만 집합에 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        
print(result)
# -


