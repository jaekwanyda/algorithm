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

#https://school.programmers.co.kr/learn/courses/30/lessons/12941
def solution(A,B):
    answer = 0
    A=sorted(A,key=lambda x:x)
    B=sorted(B,key=lambda x:-x)
    for i in range(len(A)):
        answer+=A[i]*B[i]
    return answer
