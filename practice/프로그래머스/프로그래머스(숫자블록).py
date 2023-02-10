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

#https://school.programmers.co.kr/learn/courses/30/lessons/12923
def solution(begin, end):
    answer = []
    #약수 중 가장 큰 수 찾기
    for i in range(begin,end+1):
        if i>1:
            a=1
            for j in range(2,int(i**(1/2))+1):
                if i%j==0:
                    a=j
                    if i//j<=10000000:
                        a=i//j
                        break
            answer.append(a)
        elif i==1:
            answer.append(0)
    return answer
