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
def solution(n, wires):
    #각각을 뺏을 때의 집합 갯수를 구하면 된다.
    result=[]
    for i in range(1,n):
        parent=[0]*(n+1)
        for j in range(1,n+1):
            parent[j]=j
        new_wire=wires[0:i-1]+wires[i:]
        for j in new_wire:
            union_parent(parent,j[0],j[1])
        a=parent[1]
        b=0
        for j in range(1,len(parent)):
            if parent[j]==a:
                b+=1
            else:
                b-=1
        result.append(abs(b))
    answer=min(result)
    return answer #실패


from collections import Counter
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
def solution(n, wires):
    #각각을 뺏을 때의 집합 갯수를 구하면 된다.
    result=[]
    answer=987
    for i in range(1,n):
        parent=[0]*(n+1)
        for j in range(1,n+1):
            parent[j]=j
        new_wire=wires[0:i-1]+wires[i:]
        for j in new_wire:
            union_parent(parent,j[0],j[1])
        uf = []
        for i in range(1, n + 1):
            uf.append(find_parent(parent,i))
            
        uf = Counter(uf)
        v = list(uf.values())
        answer = min(answer, abs( v[0]- v[1]))
    return answer #성공
