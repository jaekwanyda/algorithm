import sys
input = sys.stdin.readline
#아이디어: 주사위가 굴러가는 방향에 따라 list의 요소들을 바꿔주면 될 것 같다
#n,m,x,y,k 입력받기
n,m,x,y,k = map(int,input().split())
#지도 입력받기
array = [list(map(int,input().split())) for _ in range(n)]
#주사위 굴러가는 방향들 입력받기
order_list = list(map(int,input().split()))
dice = [0,0,0,0,0,0,0] #도면에서 1,2,3,4,5,6에 들어있는 수 저장하는 list
dx = [0,0,0,-1,1] #각각 동,서,북,남일 경우 이동하는 x,y 방향
dy = [0,1,-1,0,0]
for order in order_list:
    nx = x + dx[order]
    ny = y + dy[order]
    if 0<=nx<n and 0<=ny<m:
        x = nx
        y = ny
    else: #지도 밖으로 나가는 경우 생략하기
        continue
    if order == 1: #동쪽인 경우
        if array[x][y] == 0:
            array[x][y] = dice[3]
        else:
            dice[3] = array[x][y]
            array[x][y] = 0
        #주사위 내부 위치들 바꿔주기
        dice[1],dice[3],dice[4],dice[6] = dice[3],dice[6],dice[1],dice[4]
    elif order == 2: #서쪽인 경우
        if array[x][y] == 0:
            array[x][y] = dice[4]
        else:
            dice[4] = array[x][y]
            array[x][y] = 0
        #주사위 내부 위치들 바꿔주기
        dice[1],dice[3],dice[4],dice[6] = dice[4],dice[1],dice[6],dice[3]
    elif order == 4: #남쪽인 경우
        if array[x][y] == 0:
            array[x][y] = dice[5]
        else:
            dice[5] = array[x][y]
            array[x][y] = 0
        #주사위 내부 위치들 바꿔주기
        dice[1],dice[2],dice[5],dice[6] = dice[5],dice[1],dice[6],dice[2]
    elif order == 3: #북쪽인 경우
        if array[x][y] == 0:
            array[x][y] = dice[2]
        else:
            dice[2] = array[x][y]
            array[x][y] = 0
        #주사위 내부 위치들 바꿔주기
        dice[1],dice[2],dice[5],dice[6] = dice[2],dice[6],dice[1],dice[5]
    print(dice[6])