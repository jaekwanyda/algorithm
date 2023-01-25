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

def sort_key(x):
    a=len(x)
    if len(x)<4:
        while len(x)!=4:
            x+=x[0]
    if x[0]<x[1]:
        a=-a
    return (x[0],x[1],x[2],x[3],a)
def solution(numbers):
    answer = ''
    numbers=list(map(str,numbers))
    numbers=sorted(numbers,key=sort_key)
    numbers.reverse()
    answer=''.join(numbers)
    while len(answer)>1 and answer[0]=="0":
        answer=answer[1:]
    return answer
