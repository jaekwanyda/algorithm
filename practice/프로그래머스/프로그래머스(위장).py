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

def solution(clothes):
    answer = 1;dic={}
    for i,j in clothes:
        if not j in dic:
            dic[j]=1
        else:
            dic[j]+=1
    item=list(dic.items())
    for i,j in item:
        answer*=1+j
    answer-=1
    return answer
