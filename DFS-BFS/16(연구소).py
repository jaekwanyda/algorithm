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
#이코테 기출 16
#아이디어: 최대 64칸 중 임의의 3칸에 설치 후 바이러스 별로 DFS를 돌려 안전지대 수 확인하기?(시간복잡도 걱정)
#세로크기 N과 가로크기 M 입력받기
n,m=map(int,input().split())
#지도입력받기
array=[list(map(int,input().split())) for _ in range(n)]
#지도에 길 추가했을 때 
narray=[[0]*m for _ in range(n)]
#virus의 위치와 안전지대 위치 확인하기
virus_list=[]
for i in range(n):
    for j in range(m):
        if array[i][j]==2:
            virus_list.append((i,j))
safe_list=[]
for i in range(n):
    for j in range(m):
        if array[i][j]==0:
            safe_list.append((i,j))

#바이러스 퍼지는 것 함수
dx=[-1,1,0,0] #상하좌우 리스트
dy=[0,0,-1,1]
def virus_DFS(x,y):
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx>=0 and nx<n and ny>=0 and ny<m:#리스트 내에 속하는 경우
            if narray[nx][ny]==0: #안전지대일 경우만 변경
                narray[nx][ny]=2
                virus_DFS(nx,ny) #감염 시킨 경우 DFS 진행
                
#안전지대 수 구하는 함수
def count_safe(narray):
    sum=0
    for i in range(n):
        for j in range(m):
            if narray[i][j]==0:
                sum+=1
    return sum
                
#조합의 각 경우 별 진행하기
import itertools
result=0
for x in itertools.combinations(safe_list,3): #안전지대 중 3개 고르기
    #지도를 추가할 narray 새로 만들기
    for i in range(n):
        for j in range(m):
            narray[i][j]=array[i][j]
    #사다리 추가하기
    for i in range(3):
        narray[x[i][0]][x[i][1]]=1
    for i in virus_list:
        virus_DFS(i[0],i[1])
    result=max(result,count_safe(narray))
    
print(result)
# -

result


