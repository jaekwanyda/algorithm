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

import math
def solution(w,h):
    rm=0
    m=min(w,h)
    if m==h:
        w,h=h,w
    def gcd(w,h):
        a=w%h
        if a==0:
            return h
        else:
            return gcd(h,a)
    k=gcd(w,h)
    w=w//k;h=h//k
    for i in range(0,w):
        rm+=math.ceil((i+1)*h/w)-int(i*h/w)
    rm*=k
    answer=w*h*k*k-rm
    return answer
