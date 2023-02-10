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

#https://school.programmers.co.kr/learn/courses/30/lessons/12946
def solution(n):
    dp=[[[1,3]]] #n에 따른 dp 테이블 생성(n=1인 경우 넣어두기)
    for i in range(14):
        a=[]
        for d,p in dp[i]:#n-1의 하노이 탑을 2번째 기둥에 옮기기
            if d==2:
                d=3
            elif d==3:
                d=2
            if p==2:
                p=3
            elif p==3:
                p=2
            a.append([d,p])
        a.append([1,3])#n번째 원판 3번째 기둥으로 옮기기
        for d,p in dp[i]:#2번째 기둥의 n-1 하노이탑 3번째 기둥을로 옮기기
            if d==1:
                d=2
            elif d==2:
                d=1
            if p==1:
                p=2
            elif p==2:
                p=1
            a.append([d,p])
        dp.append(a)
    return dp[n-1]
