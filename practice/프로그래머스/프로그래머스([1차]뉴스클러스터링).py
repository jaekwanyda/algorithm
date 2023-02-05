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

def is_alpha(s):
    if ord(s)<ord('A') or ord(s)>ord('z') or ord('Z')<ord(s)<ord('a'):
        return False
    return True
def solution(str1, str2):
    answer = 0
    dic1={};dic2={} #dic으로 겹치는 다중원소의 개수 구해주기
    set_d=set()
    for i in range(len(str1)-1):
        if is_alpha(str1[i]) and is_alpha(str1[i+1]):
            a=str.upper(str1[i]+str1[i+1])
            if not a in dic1:
                dic1[a]=1
                set_d.add(a)
            else:
                dic1[a]=dic1[a]+1
    for i in range(len(str2)-1):
        if is_alpha(str2[i]) and is_alpha(str2[i+1]):
            a=str.upper(str2[i]+str2[i+1])
            if not a in dic2:
                dic2[a]=1
                set_d.add(a)
            else:
                dic2[a]=dic2[a]+1
    and_sum=0;or_sum=0 #교집합 개수와 합집합 개수 세기
    for i in set_d:
        if i in dic1 and i in dic2:#둘다 존재할 때
            and_sum+=min(dic1[i],dic2[i])
            or_sum+=max(dic1[i],dic2[i])
        else:
            if i in dic1:
                or_sum+=dic1[i]
            elif i in dic2:
                or_sum+=dic2[i]
    if set_d:
        answer=int(and_sum/or_sum*65536)
    else:
        answer=65536
    return answer
