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

from itertools import combinations
def solution(relation):
    combi=[]
    for i in range(1,len(relation[0])+1):
        combi+=combinations(range(len(relation[0])),i)
    uni=[] #유일한 조합만 저장할 list
    for i in combi:
        array=[tuple([row[column] for column in i]) for row in relation]
        if len(set(array))==len(relation):#uniqueness
            possi=True
            for k in uni: #uni에 속한 것들을 안가지고 있을 때 최소성 성립
                if set(k).issubset(set(i)):
                    possi=False
                    break
            if possi:
                uni+=[i]
    return len(uni)
