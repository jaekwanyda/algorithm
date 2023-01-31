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

def solution(progresses, speeds):
    answer = []
    while progresses:
        day=0
        while progresses[0]<100:
            progresses[0]+=speeds[0]
            day+=1
        for i in range(1,len(progresses)):
            progresses[i]+=day*speeds[i]
        cnt=0
        while progresses and progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1
        answer.append(cnt)
        
    return answer
