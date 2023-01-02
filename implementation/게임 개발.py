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
#아코테 구현 예제 3
n,m=map(int,input().split())
#방문한 위치를 저장하기 위한 맵을 생성
invited=[[0]*m for _ in range(n)] # 0으로 초기화 하기 위한 방법 중 하나
#현재 캐릭터의 위치와 방향 입력
x,y,direction=map(int,input().split())
invited[x][y]=1 #시작 지점 방문 처리
#맵 정보 입력받기
array=[list(map(int,input().split())) for _ in range(n)] # 잘 몰랐던 방법!!
dx =[-1,0,1,0] #일반적인 x,y,평면 생각 하면 안됨!!!! (틀린 부분) row와 column으로 생각해야 함
dy =[0,1,0,-1] #방향별 움직이는 방향

# 왼쪽으로 회전하는 함수 rot_90 생성
def rot_90():
    global direction #밖에 있는 direction 을 사용해야 하므로 global 사용하기 !! (잘 몰랐음)
    direction-=1
    if direction==-1:
        direction=3
        
count=1 #방문한 지역 수
turn_time=0 #4번 회전하면 뒤로 가야함
while (True):
    rot_90()
    next_x=x+dx[direction]
    next_y=y+dy[direction]
    # 바로 앞이 안가본 지역이고, 육지일 경우 전진
    if invited[next_x][next_y]==0 and array[next_x][next_y]==0:
        invited[next_x][next_y]=1 #방문처리 해주기 (까먹은 부분)
        x=next_x
        y=next_y
        count+=1
        turn_time=0
        continue
    #아닐 경우 한번 더 돌기    
    else:
        turn_time+=1
    if turn_time==4:
        next_x=x-dx[direction]
        next_y=y-dy[direction]
        #만약 바다라서 뒤로가지 못하면 멈추기
        if array[next_x][next_y]==1:
            break
        else:
            x=next_x
            y=next_y
            turn_time=0
print(count)
# -


