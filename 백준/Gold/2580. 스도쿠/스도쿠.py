import sys
input = sys.stdin.readline
#아이디어: 백트래킹을 이용해보자
#스도쿠 정보 입력받기
array = [list(map(int,input().split())) for _ in range(9)]
#x번째 row에 k가 있는지 확인해주는 함수
def row(x,k):
    for i in range(9):
        if array[x][i] == k:
            return False
    return True
#마찬가지로 column
def column(y,k):
    for i in range(9):
        if array[i][y] == k:
            return False
    return True
#이번엔 한 블럭 안에 있는지 여부 조사
def block(x,y,k):
    nx = (x // 3) * 3
    ny = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if array[nx+i][ny+j] == k:
                return False
    return True
#빈칸 위치들 찾아주기
zeros = []
for x in range(9):
    for y in range(9):
        if array[x][y] == 0:
            zeros.append((x,y))
#dfs 돌리기
def dfs(n):
    #만약 모든 빈칸을 다 처리했다면 처리된 스도쿠 출력
    if n == len(zeros):
        for i in range(9):
            print(*array[i])
        exit(0)
    for i in range(1,10): #스도쿠 수인 1~9까지 돌리기
        x = zeros[n][0]
        y = zeros[n][1]
        if row(x,i) and column(y,i) and block(x,y,i): #전부 포함 안되면 그때 진행
            array[x][y] = i
            dfs(n+1)
            array[x][y] = 0 #다시 백트래킹
dfs(0)