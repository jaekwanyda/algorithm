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

def solution(record):
    answer = []
    dic={}
    for i in record:
        data=i.split(' ')
        if not data[1] in dic: #없는 경우는 enter해서 처음 들어오는 경우니까 그때 닉네임 저장
            dic[data[1]]=data[2]
        else:#있는 경우에는 change나 enter의 경우에 바꿔줌
            if data[0]=='Enter' or data[0]=='Change':
                dic[data[1]]=data[2]
    for i in record:
        data=i.split(' ')
        k=''
        if data[0]=='Enter':
            k+=dic[data[1]]
            k+='님이 들어왔습니다.'
            answer.append(k)
        elif data[0]=='Leave':
            k+=dic[data[1]]
            k+='님이 나갔습니다.'
            answer.append(k)
    return answer
