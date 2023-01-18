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

def solution(k, ranges):
    answer = []
    data=[k]
    while True:
        if k%2==0:
            data.append(k//2)
            k=k/2
        else:
            data.append(k*3+1)
            k=k*3+1
        if k<=1:
            break
    dp=[0]*len(data)
    for i in range(1,len(dp)):
        dp[i]=dp[i-1]+(data[i]+data[i-1])/2
    for i,j in ranges:
        if i>len(dp)+j-1:
              answer.append(-1.0)
        else:
            answer.append(dp[-1+j]-dp[i])
    return answer
