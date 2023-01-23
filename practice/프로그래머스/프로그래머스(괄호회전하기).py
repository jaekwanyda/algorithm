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

# +
def is_correct(st): #{[}] 인 테스트 케이스 확인하기!
    dic={} 
    dic['small']=0;dic['middle']=0;dic['big']=0
    last=[]
    for inx,i in enumerate(st):
        if i=="(":
            dic['small']+=1
            last.append('small')
        if i=="{":
            dic['middle']+=1
            last.append('middle')
        if i=="[":
            dic['big']+=1
            last.append('big')
        if i==")":
            if len(last)>0:
                a=last.pop()
            else:
                return False
            dic['small']-=1
            if a!="small" or dic['small']<0:
                return False     
        if i=="}":
            dic['middle']-=1
            if len(last)>0:
                a=last.pop()
            else:
                return False
            if a!="middle" or dic['middle']<0:
                return False
        if i=="]":
            dic['big']-=1
            if len(last)>0:
                a=last.pop()
            else:
                return False
            if a!="big" or dic['big']<0:
                return False
    for i in dic:
        if dic[i]!=0:
            return False
    return True
        
def solution(s):
    answer = 0
    for i in range(len(s)):
        st=s[i:]+s[:i]
        if is_correct(st):
            answer+=1
    return answer
# -


