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
def solution(x, y, n):
    q=deque()
    q.append((y,0))#몇번 진행했는지 확인하기 위해 0 삽입
    while q:
        a,m=q.popleft()
        if a==x:
            return 0
        if a>n:
            a-=n
            if a==x:
                return m+1
            else:
                q.append((a,m+1))
            a+=n
        if a%2==0:
            a=a/2
            if a==x:
                return m+1
            else:
                q.append((a,m+1))
            a=a*2
        if a%3==0:
            a=a/3
            if a==x:
                return m+1
            else:
                q.append((a,m+1))
            a=a*3
        if len(q)==0:
            return -1
    return -1
