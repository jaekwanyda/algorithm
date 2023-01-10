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
#이코테 실전 17(백준 18405)
#아이디어: 바이러스 크기 순서대로 초마다 1칸의 BFS를 진행하면 될 것 같다.=> 고민: 초마다를 어떻게 구현해야 할까?(deque 두개 이용?)
from collections import deque
#시험관의 크기 N과 바이러스 종류 수 K입력 받기
n,k=map(int,input().split())
#시험관 정보 입력할 리스트 생성
data=[]
#시험관 정보 입력받기
for i in range(n):
    data.append(list(map(int,input().split())))
#바이러스 위치 저장할 리스트 생성
virus=[]
#바이러스 정보 입력해주기
for i in range(n):
    for j in range(n):
        if data[i][j]!=0:
            virus.append((data[i][j],i,j,0)) #0은 시간을 담을 용도

#원하는 시간, 공간 위치 입력받기
target_s,target_x,target_y=map(int,input().split())

#BFS 구현
dx=[-1,1,0,0]
dy=[0,0,-1,1]
virus.sort()
q=deque(virus)

while q:
    v,x,y,s=q.popleft()
    if s==target_s:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n : #이동 가능한 경우
            if data[nx][ny]==0:
                data[nx][ny]=v
                q.append((v,nx,ny,s+1))
                
print(data[target_x-1][target_y-1])
# -


