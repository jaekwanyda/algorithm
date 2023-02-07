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

#https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    answer = []
    word_set=set();word_set.add(words[0]) #첫번째 word를 저장한 set 생성
    for i in range(1,len(words)):
        word=words[i]
        #이전 word의 마지막 글자와 이번 word의 첫 글자가 다르거나 word가 이미 word_set에 있으면 멈춤
        if word in word_set or word[0]!=words[i-1][-1]:
            answer=[i%n+1,i//n+1]
            break
        else:
            word_set.add(word)
        if i==len(words)-1: #만약 끝까지 진행된다면
            answer=[0,0]
    return answer
