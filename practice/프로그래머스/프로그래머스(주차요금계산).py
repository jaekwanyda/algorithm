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

import math
def solution(fees, records):
    answer = []
    #딕셔너리에 정리해두기
    dic={}
    a="05"
    for i in records:
        if not i[6:10] in dic:
            dic[i[6:10]]=[int(i[0:2])*60+int(i[3:5])]
        else:
            dic[i[6:10]].append(int(i[0:2])*60+int(i[3:5]))
    dic=sorted(dic.items(),key=lambda x:x[0])
    for car in dic:
        if len(car[1])%2==1:
            car[1].append(23*60+59)
    for car in dic:
        total_time=0
        a=-1
        for t in car[1]:
            total_time+=a*t
            a*=-1
        print(total_time)
        if total_time>fees[0]:
            answer.append(fees[1]+math.ceil((total_time-fees[0])/fees[2])*fees[3])
        else:
            answer.append(fees[1])
    return answer
