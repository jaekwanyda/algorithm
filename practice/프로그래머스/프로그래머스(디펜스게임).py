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

# 배운점: heapq 사용에 익숙해지자
import heapq
def solution(n, k, enemy):
    q=[]
    sum_enemy=0;end_round=0
    for num in enemy:
        sum_enemy+=num
        heapq.heappush(q,-num)
        if sum_enemy<=n:
            end_round+=1
        elif k>0:
            k-=1
            sum_enemy+=heapq.heappop(q)
            end_round+=1
        else:
            break
    return end_round
