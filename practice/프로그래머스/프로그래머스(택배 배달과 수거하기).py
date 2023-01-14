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
def one_way(array,cap):
    if len(array)==0:
        return array
    x,y=array.pop()
    if cap-y<0:
        array.append((x,y-cap))
    elif cap-y==0:
        return array
    else:
        array=one_way(array,cap-y)
    return array
        
            

def solution(cap, n, deliveries, pickups):
    answer = []
    #그리디 문제: 가장 멀리 있는 집 부터 해결하면 된다.
    q=[] #배달 상자가 있는 집
    p=[] #수거할 상자가 있는 집
    for i in range(n):
            if deliveries[i]!=0:
                q.append((i+1,deliveries[i]))
            if pickups[i]!=0:
                p.append((i+1,pickups[i]))
    while (q or p):
        if len(q)>0 and len(p)>0:
            answer.append(max(q[len(q)-1][0],p[len(p)-1][0]))
        elif len(q)==0:
            answer.append(p[len(p)-1][0])
        else:
            answer.append(q[len(q)-1][0])
        p=one_way(p,cap)
        q=one_way(q,cap)
    return 2*sum(answer)
