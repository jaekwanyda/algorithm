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
#이코테 그래프 예제 3
#아이디어 : 크루스칼 알고리즘으로 최저 비용의 길을 찾고 제일 비용이 높은 것 하나만 없앤다.
def find_parent(parent,a):
    if parent[a]!=a:
        parent[a]=find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent,a,b):
    #더 작은 번호의 부모에 편입
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a #루트 노드 바꾸기(의문: 이렇게 바꾸면 자식 노드들은 아직 업데이트가 안됨. 뒤에서 find함수를 다 돌려줘야 할듯)
    else:
        parent[a]=b
#N,M 입력받기
n,m =map(int,input().split())

import heapq
q=[]
#간선을 heapq에 저장해 오름차순으로 정렬되게 함.
for _ in range(m):
    a,b,cost=map(int,input().split())
    heapq.heappush(q,(cost,a,b)) #cost를 기준으로 정렬하기 위함

result=[] #비용을 리스트로 저장하여 마지막 빼고 다 더해줄 거임.
parent=[0]*(n+1)
#부모 리스트 자기 자신으로 초기화
for i in range(n+1):
    parent[i]=i

while q:
    cost,a,b=heapq.heappop(q)
    #사이클 발생여부에 따라 추가
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result.append(cost)

result=result[0:-1]
print(sum(result))
# -


