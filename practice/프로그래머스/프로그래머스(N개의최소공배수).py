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

def solution(arr):
    answer = 1
    def gcd(a,b):
        c=a%b
        if c==0:
            return b
        else:
            return gcd(b,c)
    def lcm(a,b):
        return a/gcd(a,b)*b
    for a in arr:
        answer=lcm(answer,a)
    return answer
