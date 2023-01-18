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

def solution(topping):
    n=len(topping)
    top_set=set()
    back_data=set()
    back_data.add(topping[n-1])
    back_array=[0]*(len(topping))
    back_array[0]=1
    answer=0
    for i in range(1,n):
        if not topping[n-1-i] in back_data:
            back_data.add(topping[n-1-i])
        back_array[i]=len(back_data)
        
    for i in range(n-1):
        top_set.add(topping[i])
        if len(top_set)==back_array[-i-2]:
            answer+=1
    return answer
