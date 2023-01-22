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

def is_prime(k):
    a=True
    if k==1 or k==0:
        a=False
    for i in range(2,int(k**(1/2))+1):
        if k%i==0:
            a=False
    return a
def solution(n, k):
    answer = 0
    k_list=[]
    cnt=1
    while True:
        if n/(k**cnt)>1:
            cnt+=1
        else:
            break
    for i in range(cnt):
        k_list.append(n//(k**(cnt-i-1)))
        n%=k**(cnt-i-1)
    data=[];sum_=0
    for i,num in enumerate(k_list):
        if num!=0 and i<len(k_list)-1:
            sum_=sum_*10+num
        elif num==0:
            data.append(sum_)
            sum_=0
        else:
            sum_=sum_*10+num
            data.append(sum_)
    for i in data:
        if is_prime(i):
            answer+=1
    
    return answer
