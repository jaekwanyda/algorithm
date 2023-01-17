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

def solution(k, tangerine):
    answer = 0
    dic={}
    for i in tangerine:
        if not i in dic:
            dic[i]=1
        else:
            dic[i]+=1
    dic_item=dic.items()
    dic_item=sorted(dic_item,key=lambda x: -x[1])
    cnt=0;tan_sum=0
    for i,j in dic_item:
        tan_sum+=j
        cnt+=1
        if tan_sum>=k:
            answer=cnt
            break
    return answer
