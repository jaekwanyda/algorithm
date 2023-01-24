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
def solution(numbers, target):
    answer = 0;q=deque()
    q.append((0,0))
    while q:
        s,n=q.popleft()
        if n==len(numbers):
            if s==target:
                answer+=1
        elif n<len(numbers):
            s+=numbers[n]
            q.append((s,n+1))
            s-=2*numbers[n]
            q.append((s,n+1))
    return answer
