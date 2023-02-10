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

#https://school.programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    #투포인터를 이용해보자
    answer = 0
    pnt1=1;pnt2=2
    while pnt1<pnt2:
        s=sum(range(pnt1,pnt2))
        if s<n:
            pnt2+=1
        elif s>n:
            pnt1+=1
        elif s==n:
            answer+=1
            pnt1+=1
    return answer
