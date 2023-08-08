import sys
input = sys.stdin.readline
#아이디어: dfs를 사용하면 충분히 해결할 수 있을 것 같다.
#n,m 입력받기
n,m = map(int,input().split())
#map 입력받기
array = []
for _ in range(n):
    array.append(list(input()))
def bfs(x,y):
    #원본 문자열
    original = array[x][y]
    #오른쪽과 아래가 original과 다르면 싸이클 불가능
    if array[x+1][y] != original or array[x][y+1] != original:
        return False
    q = [(x+1,y)]
    #목적지
    target = (x,y+1)
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = True
    while q :
        a,b = q.pop()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            #만약 목적지에 도착 가능하면 True return
            if na == target[0] and nb == target[1]:
                return True
            #시작 점보다 오른쪽 아래만 보면 된다
            if x<=na<n and y<=nb<m and array[na][nb] == original and not visited[na][nb]:        
                visited[na][nb] = 1
                q.append((na,nb))
    return False
possi = False
for i in range(n-1):
    for j in range(m-1):
        if bfs(i,j):
            possi = True
if possi:
    print('Yes')
else:
    print('No')            

    