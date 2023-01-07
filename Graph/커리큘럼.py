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

# +
#이코테 그래프 예제 4
#아이디어: 위상정렬 알고리즘으로 각 값의별 합을 구해준다. 다이나믹도 이용하면 좋을 것 같다.
from collections import deque
import copy #리스트값을 그대로 복사할 때는 copy함수 이용해주기!! (새로 배운 것)

#노드 갯수 입력받기
n=int(input())

#모든 노드에 대한 진입차수 0으로 초기화
indegree=[0]*(n+1)
#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph=[[] for _ in range(n+1)]
#각 강의 시간을 0으로 초기화
time=[0]*(n+1)

#방향 그래프의 모든 간선 정보 입력받기
for i in range(1,n+1):
    data=list(map(int,input().split())) #입력 길이가 일정하지 않기에 list로 받기
    time[i]=data[0] #입력 정보의 첫번째는 강의의 시간
    for j in data[1:-1]:
        graph[j].append(i) #이어진 간선 정보 업데이트
        indegree[i]+=1

def topology_sort():
    q=deque()
    result=copy.deepcopy(time) #시간정보가 있는 리스트 그대로 복사
    
    for i in range(1,n+1):
        if indegree[i]==0: #진입차수가 0인 수를 큐에 추가
            q.append(i) 
    while q: #q가 빌때까지 실시
        now=q.popleft()
        for i in graph[now]: #now노드와 연결되어 있는 각각의 노드들에 대해 처리
            indegree[i]-=1
            if indegree[i]==0:#진입차수가 0이되면 큐에 추가하고 시간을 더해준다.
                result[i]+=result[now] #책의 풀이에는 result[i]=max(result[i],result[now]+time[i])로 나와있다.
                q.append(i)
                
    for i in range(1,n+1):
        print(result[i])

topology_sort()
