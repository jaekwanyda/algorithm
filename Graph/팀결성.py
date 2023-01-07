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
#이코테 연습문제 2번
#서로소 집합 이용
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
        
#n,m 입력받기
n,m=map(int,input().split())
#부모 리스트 생성
parent=[0]*(n+1) #총 n+1개이다. 0번도 이용

for i in range(n+1):
    parent[i]=i #자기 자신으로 초기화


#연산 입력받기
for i in range(m):
    a,b,c=map(int,input().split()) # a는 연산 종류, b,c는 학생 번호
    if a==0:
        union_parent(parent,b,c)
    else:
        a=find_parent(parent,a)
        b=find_parent(parent,b)
        print(parent)
        if a==b:
            print("YES")
        else:
            print("NO")    
            
parent
# -


