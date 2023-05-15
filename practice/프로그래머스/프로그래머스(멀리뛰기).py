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

#https://school.programmers.co.kr/learn/courses/30/lessons/12914
def solution(n):
    dp=[0]*2001
    dp[1]=1
    for i in range(2,2001):
        dp[i]=(dp[i-1]+dp[i-2])%1234567
    return dp[n+1]
