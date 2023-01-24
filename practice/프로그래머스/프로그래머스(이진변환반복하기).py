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

def sc(n):
    k=[]
    while True:
        if n<=1:
            k.append(n%2)
            break
        k.append(n%2)
        n=n//2
    k.reverse()
    return k
def solution(s):
    answer = []
    cnt=0;zero=0
    while cnt<5:
        if s=='1':
            break
        a=''
        for i in s:
            if i=='0':
                zero+=1
            else:
                a+=i
        b=len(a)
        f=''
        for i in sc(b):
            f+=str(i)
        s=f
        cnt+=1
    answer+=[cnt,zero]
    return answer
