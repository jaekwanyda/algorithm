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

def solution(elements):
    sum_ele=sum(elements)
    answer=set()
    answer.add(sum_ele)
    for i in range(1,len(elements)): #자를 길이
        for j in range(len(elements)-i+1):
            answer.add(sum(elements[j:j+i]))
            answer.add(sum_ele-sum(elements[j:j+i]))
    return len(answer)
