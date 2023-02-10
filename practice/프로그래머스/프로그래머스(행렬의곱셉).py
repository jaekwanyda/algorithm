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

#https://school.programmers.co.kr/learn/courses/30/lessons/12949
def solution(arr1, arr2):
    answer = [];row=len(arr1);column=len(arr2[0])
    for i in range(row):
        a=[]
        for j in range(column):
            b=0
            for k in range(len(arr1[0])):
                b+=arr1[i][k]*arr2[k][j]
            a.append(b)
        answer.append(a)
    return answer
