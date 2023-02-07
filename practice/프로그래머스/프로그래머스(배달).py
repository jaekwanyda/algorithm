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

#https://school.programmers.co.kr/learn/courses/30/lessons/12978https://school.programmers.co.kr/learn/courses/30/lessons/12978
import heapq
def solution(N, road, K):
    answer = 0
    #다익스트라로 해결해보자(heapq이용)
    graph=[[] for _ in range(N+1)] #N개의 마을과 연결된 간선 정보 저장할 list
    inf=987654321
    distance=[inf]*(N+1) #거리 저장할 list
    distance[1]=0
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c)) #a,b와 연결된 길이 c인 간선 정보 저장
    q=[]
    heapq.heappush(q,(0,1)) #거리와 시작 마을 정보 입력
    while q:
        dist,now=heapq.heappop(q) #가장 짧은 거리와 연결된 노드
        if distance[now]<dist: #이미 더 짧은게 존재하면 생략
            continue
        for i in graph[now]:#현재 연결된 노드와 연결된 것들의 거리와 노드 확인
            new_dist=dist+i[1]
            if new_dist<distance[i[0]]: #새로운 거리가 기존 것 보다 짧을 때
                distance[i[0]]=new_dist
                heapq.heappush(q,(new_dist,i[0]))
    for dis in distance:
        if dis<=K: answer+=1
    return answer
