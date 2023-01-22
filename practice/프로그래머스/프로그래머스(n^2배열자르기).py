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

def find(n,a):
    row=(a//n)+1
    column=(a%n)+1
    return max(row,column)
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(find(n,i))
    return answer
