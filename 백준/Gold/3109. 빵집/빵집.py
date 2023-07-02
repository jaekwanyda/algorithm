import sys
input = sys.stdin.readline
#아이디어: 최대한 위에 것들 끼리 이어주기
#R,C 입력받기
r,c = map(int,input().split())
#array 입력받기
array = [list(input().rstrip()) for _ in range(r)]
#방문 여부 확인하기
visited = [[False]*c for _ in range(r)]
dx = [-1,0,1] #x는 이 3가지로 이동 가능, y는 무조건 +1
#갈 수 있는 최선의 위 경로 확인
answer = 0
def dfs(x,y):
    #마지막 점에 도착했을 때 멈추기
    global answer
    if y == c-1:
        answer += 1
        return True
    for i in range(3):
        nx = x+dx[i]
        ny = y+1
        #가능한 지점이면 이동
        if 0<=nx<r and array[nx][ny]=='.':
            if visited[nx][ny] == 0:
                #이미 방문한 지점에서 만약 뒤로 진행이 불가능할 경우는 굳이 안봐도 되므로 방문 처리
                visited[nx][ny] =1
                if dfs(nx,ny):
                    return True
    return False
for i in range(r):
    dfs(i,0)
print(answer)
