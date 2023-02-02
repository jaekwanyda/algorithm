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

def solution(msg):
    answer = [];dic={};cnt=1
    dic_list=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in dic_list:
        dic[i]=cnt
        cnt+=1
    array=list(msg)
    while array:
        a=array.pop(0)
        if not array:
            answer.append(dic[a])
        while array:
            if a+array[0] in dic:
                a+=array.pop(0)
                if not array:
                    answer.append(dic[a])
            else:
                dic[a+array[0]]=cnt
                cnt+=1
                answer.append(dic[a])
                break    
    return answer
