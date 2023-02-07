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

#https://school.programmers.co.kr/learn/courses/30/lessons/12985
def solution(n,a,b):
    answer = 0
    #이진트리 문제. 가장 작은 부모 노드를 찾으면 해결
    while a!=b:
        a=(a+1)//2;b=(b+1)//2
        answer+=1

    return answer
