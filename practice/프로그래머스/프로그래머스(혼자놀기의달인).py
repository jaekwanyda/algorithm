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

def solution(cards):
    n=len(cards)
    parent=[0]*(n+1)
    def find_parent(parent,a):
        if parent[a]!=a:
            parent[a]=find_parent(parent,parent[a])
        return parent[a]
    def union_parent(parant,a,b):
        a=find_parent(parent,a)
        b=find_parent(parent,b)
        if a!=b:
            if a<b:
                parent[b]=a
            else:
                parent[a]=b
    visited=[False]*(n+1)
    for i in range(1,n+1):
        parent[i]=i
    visited[0]=True
    for i,j in enumerate(cards):
        if not visited[j]:
            union_parent(parent,j,cards[j-1])
            visited[j]=True
    for i in range(n+1):
        parent[i]=find_parent(parent,i)
    card_dic={}
    for i in parent:
        if not i in card_dic:
            card_dic[i]=1
        else:
            card_dic[i]+=1
    data=sorted(card_dic.items(),key=lambda x:-x[1])
    if len(data)==2:
        answer=0
    else:
        answer=data[0][1]*data[1][1]
    return answer
