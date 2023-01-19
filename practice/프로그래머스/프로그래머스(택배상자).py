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

def solution(order):
    answer=1
    con=[0]*len(order)
    for i in range(len(order)):
        con[i]=i+1
    sub_con=con[:order[0]-1]
    idx=1
    b=order[0]
    while idx<len(order):
        if order[idx]>order[idx-1]:
            sub_con=sub_con+con[b:order[idx]-1]
            answer+=1
            b=order[idx]
            idx+=1
        else:
            a=sub_con.pop()
            if a==order[idx]:
                answer+=1
                idx+=1
            else:
                break
    
    return answer
