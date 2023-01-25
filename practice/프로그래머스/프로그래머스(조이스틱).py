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

def solution(name):
    answer = 0
    test=[]
    for n in name:
        test.append(min(ord(n)-ord('A'),ord('Z')-ord(n)+1))
    min_sum=len(name)-1
    for i,j in enumerate(test):
        if j==0:
            n=1
            while i+n<len(test) and test[i+n]==0:#몇번의 0이 반복되는지 확인
                n+=1
            #0이 나왔을 때 생략할 수 있는 횟수 업데이트
            if i>0:
                min_sum=min(min_sum,2*(i-1)+len(name)-(i+n),2*(len(name)-(i+n))+(i-1))
            
    
    return min_sum+sum(test)
