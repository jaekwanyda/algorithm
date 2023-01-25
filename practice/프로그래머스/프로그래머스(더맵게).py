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
def solution(scoville, K):
    answer = 0;q=sorted(scoville)
    heapq.heappush(q,0)
    heapq.heappop(q)
    while q:
        a=heapq.heappop(q)
        if a>=K:
            break
        if len(q)==0:
            answer=-1
            break
        b=heapq.heappop(q)
        heapq.heappush(q,a+b*2)
        answer+=1
    return answer
