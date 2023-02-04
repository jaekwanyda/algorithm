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

#https://school.programmers.co.kr/learn/courses/30/lessons/17680
#LRU 알고리즘은 가장 최근에 사용한 캐쉬를 가장 앞으로 옮겨주는 알고리즘
#간단하게 hit 했을 경우에는 해당되는 요소를 head 쪽으로 miss의 경우 마지막에 들어온 것을 head로 옮긴다.
def solution(cacheSize, cities):
    answer = 0;cache=[]
    while cities:#cache를 이용해 hit,miss 여부 체크
        city=str.upper(cities.pop(0))
        if city in cache:#hit의 경우
            answer+=1
            for i,j in enumerate(cache):#hit된 원소를 head로 옮기기(나는 list의 마지막을 head로 정했다.)
                if j==city:
                    cache.pop(i);
                    break
            cache.append(city)
        else:#miss의 경우
            answer+=5
            if len(cache)<cacheSize: #cache 채워주기
                cache.append(city)
            else:
                if cache:
                    cache.pop(0);cache.append(city)
        
    return answer
