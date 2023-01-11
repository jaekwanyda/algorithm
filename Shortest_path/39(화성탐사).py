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

#이코테 실전 39
#아이디어: 탐사기계는 아래로 내려가거나, 오른쪽으로 가거나 두 행동 중에 하나만 할 수 있다.(틀림! 상하좌우로 가능)=>조건 조심해야한다.
#다이나믹을이용해 가능한 모든 경우 중 가장 작은 경우를 출력해보자
#테스트 수 T입력받기
t=int(input())
for i in range(t):
    #n 입력받기
    n=int(input())
    #에너지양 입력받기
    data=[list(map(int,input().split())) for _ in range(n)]
    INF=987654321
    dp=[[INF]*n for _ in range(n)] #dp테이블 초기화
    dp[0][0]=data[0][0]
    
    for i in range(n):
        for j in range(n):
            if i==0 and j!=0: #열이 첫번째 일땐 왼쪽에서 오는 경우밖에 없음
                dp[i][j]=data[i][j]+dp[i][j-1]
            elif j==0 and i!=0:#행이 첫번째 일땐 위에서 오는 경우밖에 없음
                dp[i][j]=data[i][j]+dp[i-1][j]
            elif j>0 and i>0:#이외의 경우에는 위, 왼쪽에서 오는 경우 중 작은 것을 채택한다.
                dp[i][j]=data[i][j]+min(dp[i-1][j],dp[i][j-1]) 
    print(dp[n-1][n-1])

#위는 틀린 풀이로 두번째 풀이 작성.
#이 문제는 다익스트라로 상하좌우 최선의 길을 찾아가면 해결된다. 
import heapq
t=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(t):
    #n 입력받기
    n=int(input())
    #에너지양 입력받기
    data=[list(map(int,input().split())) for _ in range(n)]
    INF=987654321
    distance=[[INF]*n for _ in range(n)] #distance테이블 초기화
    q=[(data[0][0],0,0)] #처음 위치를 큐에 삽입
    distance[0][0]=data[0][0]
    while q: #q가 빌때까지
        dis,x,y=heapq.heappop(q) #거리와 위치 정보 받기
        if distance[x][y]<dis: #처리가 완료된 경우 넘어간다
            continue
        for i in range(4): #이동가능한 상하좌우 좌표에 대해 확인
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                n_distance=dis+data[nx][ny] #자신을 거쳐서 (nx,ny)로 가는 경우
                if n_distance<distance[nx][ny]: #기존의 경로보다 짧을 경우
                    distance[nx][ny]=n_distance
                    heapq.heappush(q,(n_distance,nx,ny))
    print(distance[n-1][n-1])


