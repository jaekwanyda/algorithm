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
#간단한 아이디어로 사이클 여부를 확인할 수 있다.
#아이디어: 간선별로 연결된 노드의 parent를 확인해서 만약 같은 parent면 사이클 존재
#노드의 개수와 간선의 개수 입력
v,e=map(int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i # 부모를 자기 자신으로 초기화

cycle=False

for i in  range(e):
    a,b=map(int,input().split())
    
    #사이클이 생긴경우 종료
    if parent[a]==parent[b]:
        cycle=True
        break
    else:
        union_parent(parent,a,b)
        
if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다")
# -


