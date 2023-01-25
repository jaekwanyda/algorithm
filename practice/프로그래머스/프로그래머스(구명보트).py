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

from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    q=deque(people);cnt=0
    while q:
        if len(q)==1:
            answer+=1
            break
        max_=q.pop()
        min_=q.popleft()
        if max_+min_>limit:
            q.appendleft(min_)
            cnt+=1
        else:
            cnt+=2
        answer+=1
    return answer
