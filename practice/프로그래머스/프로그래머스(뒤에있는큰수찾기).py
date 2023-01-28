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

import heapq
from collections import deque
def solution(numbers):
    answer = [-1]*len(numbers)
    q=[]
    heapq.heappush(q,(numbers[0],0))
    num_que=deque(numbers)
    num_que.popleft()
    i=1
    while num_que:
        i1=num_que.popleft()
        while True:
            if len(q)==0:
                break
            i0,idx=heapq.heappop(q)
            if i0<i1:
                answer[idx]=i1
            else:
                heapq.heappush(q,(i0,idx))
                break
        if answer[i]==-1:
            heapq.heappush(q,(i1,i))
        i+=1
    return answer
