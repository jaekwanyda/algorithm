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

from itertools import permutations
def is_prime(n):
    if n==1 or n==0:
        return False
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True
def solution(numbers):
    answer = []
    for i in range(1,len(numbers)+1):
        per=permutations(numbers,i)
        for p in per:
            k=''.join(p)
            if is_prime(int(k)):
                answer.append(k)
    
    for i in range(len(answer)):
        while len(answer[i])>0 and answer[i][0]=='0':
            answer[i]=answer[i][1:]
    return len(set(answer))
