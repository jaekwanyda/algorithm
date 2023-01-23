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

from collections import deque
def solution(places):
    answer = []
    for place in places:
        q=deque();m=0 #거리두기 안지킨 사람 세기
        dx=[-1,1,0,0];dy=[0,0,-1,1]
        for i,k in enumerate(place):
            for j in range(5):
                if k[j]=='P':
                    q.append((i,j,(i,j),0))
        while q:
            x,y,start,n=q.popleft()
            if n>=2:
                break
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx>=0 and nx<5 and ny>=0 and ny<5:
                    if place[nx][ny]=="O" and (nx,ny)!=start:
                        q.append((nx,ny,start,n+1))
                    elif place[nx][ny]=="P" and (nx,ny)!=start:
                        m+=1
        if m>0:
            answer.append(0)
        else:
            answer.append(1)
                        
    return answer
