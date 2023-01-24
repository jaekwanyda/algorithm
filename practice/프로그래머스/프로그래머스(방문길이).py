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

def solution(dirs):
    answer = 0
    dx_dy={'U':[0,1],"D":[0,-1],"L":[-1,0],"R":[1,0]}
    route=set()
    x=0;y=0
    for i in dirs:
        dx,dy=dx_dy[i]
        nx=dx+x;ny=dy+y
        if nx<=5 and nx>=-5 and ny<=5 and ny>=-5:
            route.add((x,y,nx,ny))
            route.add((nx,ny,x,y))
            x=nx;y=ny
    answer=len(route)/2
    return answer
