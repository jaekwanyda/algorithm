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

def solution(priorities, location):
    answer = 0 ;stack=[]
    for i,j in enumerate(priorities):
        stack.append((i,j))
    while stack:
        idx1,prior1=stack.pop(0);possi=True
        for idx2,prior2 in stack:
            if prior1<prior2:
                possi=False
        if possi:
            answer+=1
            if idx1==location:
                break
        else:
            stack.append((idx1,prior1))
        
    return answer
