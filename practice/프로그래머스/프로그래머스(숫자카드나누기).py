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

def check_impossi(array,a):
    impossi=True
    for i in array:
        if i%a==0:
            impossi=False
    return impossi
def gcd(a,b):
    c=b%a  
    if c!=0:
        return gcd(c,a)
    else:
        return a
def solution(arrayA, arrayB):
    answer = 0

    if len(arrayA)>=1 and len(arrayB)>=1:
        gcd_A=arrayA[0]
        for i in range(len(arrayA)):
            gcd_A=gcd(gcd_A,arrayA[i])
        gcd_B=arrayB[0]
        for i in range(1,len(arrayB)):
            gcd_B=gcd(gcd_B,arrayB[i])
        if check_impossi(arrayB,gcd_A):
            answer=max(answer,gcd_A)
        if check_impossi(arrayA,gcd_B):
            answer=max(answer,gcd_B)
    else:
        a=gcd(arrayA[0],arrayB[0])
        answer=max(arrayA[0]//a,arrayB[0]//a)
    return answer
