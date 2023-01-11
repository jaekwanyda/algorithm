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
#이코테 실전 44
#아이디어: 각각의 행성별 길이를 재는 것은 수가 너무 크다.10^10 정도의 크기를 갖는다
#각각의 행성별 길이를 구한다면, 크루스칼 알고리즘으로 바로 해결될 것 같다.
#답지 참고!! x축으로 정렬했을 때의 N-1개의 간선, y,z 축에서의 N-1개의 간선 총 3(N-1) 개의 간선을 사용하면 구할 수 있다.
#왜냐하면 그 간선들은 각각의 노드에 항상 최단 거리이기 때문이다.
#크루스칼 알고리즘을 위한 서로소 집합 정의
def find_parent(parent,a):
    if parent[a]!=a:
        parent[a]=find_parent(parent,parent[a])
    return parent[a]
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#행성 개수 n입력 받기
n=int(input())

parent=[0]*(n+1)

for i in range(n+1):
    parent[i]=i #부모 노드는 자기 자신으로 초기화
    
#행성 정보 입력받기
data_x=[]
data_y=[]
data_z=[]
for i in range(n):
    x,y,z=map(int,input().split())
    data_x.append((x,i+1))#좌표와 행성 번호 
    data_y.append((y,i+1))
    data_z.append((z,i+1))
data_x.sort()
data_y.sort()
data_z.sort()

edges=[]
for i in range(1,n):#간선 정보 입력하기
    edges.append(((data_x[i][0]-data_x[i-1][0]),data_x[i][1],data_x[i-1][1])) #x축에서 행성 간 연결 비용, 연결된 행성들 번호 append
    edges.append(((data_y[i][0]-data_y[i-1][0]),data_y[i][1],data_y[i-1][1])) #y
    edges.append(((data_z[i][0]-data_z[i-1][0]),data_z[i][1],data_z[i-1][1])) #z
    
edges.sort()

total_cost=0
for edge in edges:
    cost,x,y=edge
    if find_parent(parent,x)!=find_parent(parent,y): #서로소 집합이라면 union
        union_parent(parent,x,y)
        total_cost+=cost
        
print(total_cost)
# -


