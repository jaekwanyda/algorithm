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

#https://school.programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    ans = 0
    #dp를 쓸까 했지만 10억 개의 리스트는 공간 복잡도 문제가 발생한다=>그때그때 처리
    while n>0:
        if n%2==0:
            n/=2
        else:
            n-=1
            ans+=1
    return ans
