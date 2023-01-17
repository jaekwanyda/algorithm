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

def solution(k, d):
    answer = 0
    for i in range(0,d+1,k):
        answer+=int((d**2-i**2)**(1/2))//k+1
    return answer
