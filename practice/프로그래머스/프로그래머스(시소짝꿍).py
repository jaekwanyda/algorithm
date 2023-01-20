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

def solution(weights): #첫 구현 : 틀림(실수부분 제외)
    answer = 0 
    siso={}
    for i in weights:
        if not i in siso:
            siso[i]=1
        else:
            siso[i]+=1
    for i in siso:
        if siso[i]>1:
            answer+=siso[i]*(siso[i]-1)
        for k in range(2,5):
            if i%k==0:
                a=i//k
                for j in range(2,5):
                    if j!=k:
                        if j*a in siso:
                            answer+=siso[i]*siso[j*a]
    return answer//2


def solution(weights):
    answer = 0
    siso={}
    for i in weights:
        if not i in siso:
            siso[i]=1
        else:
            siso[i]+=1
    for i in siso:
        if siso[i]>1:
            answer+=siso[i]*(siso[i]-1)/2
        if (i/2)*3 in siso:
            answer+=siso[i]*siso[(i/2)*3]
        if (i/2)*4 in siso:
            answer+=siso[i]*siso[(i/2)*4]
        if (i/3)*4 in siso:
            answer+=siso[i]*siso[(i/3)*4]
    return answer
