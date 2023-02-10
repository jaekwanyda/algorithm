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

#https://school.programmers.co.kr/learn/courses/30/lessons/12951#
def solution(s):
    answer = ''
    s_list=list(s.split(' '))#공백을 기준으로 문자열 나누기
    num_list=['0','1','2','3','4','5','6','7','8','9']
    print(s_list)
    for s_ in s_list:
        if len(s_)>0:
            if s_[0] not in num_list: #첫번째 글자가 알파벳일 경우만 대문자로
                answer+=str.upper(s_[0])
            else:
                answer+=s_[0]
            for i in range(1,len(s_)):#나머지는 소문자로
                answer+=str.lower(s_[i])
            answer+=' '
        else: #만약 공백이 존재하면 공백 추가
            answer+=' '
    if answer[-1]==' ':
        answer=answer[:-1]
    return answer
