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

max_=0
def dfs(p,visited,dungeons,m):
    global max_
    for i,j in enumerate(dungeons):
        if m>max_:
            max_=m
            print(max_)
        if not visited[i]:
            if p>=j[0]:
                visited[i]=True
                p-=j[1]
                m+=1
                dfs(p,visited,dungeons,m)
                visited[i]=False
                p+=j[1]
                m-=1
def solution(k, dungeons):
    global max_
    answer = -1
    n=len(dungeons)
    visited=[False]*n;m=0
    dfs(k,visited,dungeons,m)
    answer= max_
        
    
    return answer
