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
    while len(x)<20:
        x+='0'
    return (x[i] for i in range(20))
def solution(phone_book):
    answer = True
    array=sorted(phone_book)
    for i in range(len(phone_book)-1):
        a=array[i];b=array[i+1]
        if len(a)<len(b):
            if b[:len(a)]==a:
                return False
        elif len(a)>len(b):
            if a[:len(b)]==b:
                return False
    return answer
