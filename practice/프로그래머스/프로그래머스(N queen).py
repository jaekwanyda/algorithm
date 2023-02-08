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

#https://school.programmers.co.kr/learn/courses/30/lessons/12952
from collections import deque
def solution(n):
    answer = 0
    q=deque()
    #맨 위의 열에서 Q를 고정시키고 가능한 아래열로 bfs돌리기
    for i in range(1,n+1):
        q.append([i])
    while q:
        a=q.popleft()
        if len(a)==n:#만약 마지막 열까지 가능한 경우 더해주기
            answer+=1
        else:
            k=[i for i in range(1,n+1)]
            possi_set=set(k);impossi_set=set()#가능한 집합에서 불가능한 수들을 빼기
            for i,j in enumerate(a):
                impossi_set.add(j);impossi_set.add(j+(len(a)-i))
                impossi_set.add(j-(len(a)-i))
            for i in possi_set-impossi_set:#남아있는 가능한 것들을 추가해서 q에 더해주기
                q.append(a+[i])
    return answer
