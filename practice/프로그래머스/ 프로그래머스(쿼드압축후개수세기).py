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
    answer = [0,0]
    length=len(arr)
    def check_(a,b,l):
        start=arr[a][b]
        for i in range(a,a+l):
            for j in range(b,b+l):
                if arr[i][j]!=start:
                    l=l//2
                    check_(a,b,l)
                    check_(a,b+l,l)
                    check_(a+l,b,l)
                    check_(a+l,b+l,l)
                    return
        answer[start]+=1
    
    check_(0,0,length)
                    
    return answer
