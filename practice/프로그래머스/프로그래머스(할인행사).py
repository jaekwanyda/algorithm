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

def solution(want, number, discount): #for 구문에 if 구문을 통해 좀 더 간단하게 작성 가능할 것 같다.
    answer = 0
    want_dic=dict(zip(want,number))
    print(want_dic)
    dis={}
    for i in range(10):
        if not discount[i] in dis:
            dis[discount[i]]=1
        else:
            dis[discount[i]]+=1
    if want_dic==dis:
        answer+=1
    for i in range(10,len(discount)):
        dis[discount[i-10]]-=1
        if dis[discount[i-10]]==0:
            del dis[discount[i-10]]
        if not discount[i] in dis:
            dis[discount[i]]=1
        else:
            dis[discount[i]]+=1
        if want_dic==dis:
            answer+=1
        
    return answer
