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
#이코테 실전 42
#아이디어: 서로소 집합 구조 이용. 비행기가 들어왔을때 부모노드와 바로 왼쪽 노드를 union 만약 부모노드가 0이면 멈춤(몰라서 답지 봄!)

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

#탑승구수 g
g=int(input())
#비행기수 p
p=int(input())

parent=[0]*(g+1)
for i in range(1,g+1):
    parent[i]=i #부모노드는 자신으로 초기화
#비행기 정보 입력
result=0
for i in range(p):
    data=int(input())
    a=find_parent(parent,data)
    if a!=0:
        union_parent(parent,a,a-1)
        result+=1
    else:
        break

print(result)
# -


