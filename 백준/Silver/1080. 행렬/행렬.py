import sys
input = sys.stdin.readline
#아이디어: 처음부터 보면서 다르면 뒤집는다. 만약 끝까지 다 돌렸는데 다르다면 -1출력
n,m = map(int,input().split())
array_n = []
for _ in range(n):
    array_n.append(list(map(int,input().rstrip())))
array_m = []
for _ in range(n):
    array_m.append(list(map(int,input().rstrip())))
def flip(x,y):#x,y좌표에서 3*3행렬 뒤집는 함수
    for i in range(x,x+3):
        for j in range(y,y+3):
            array_n[i][j] = 1 - array_n[i][j]
cnt = 0
for x in range(n-2):
    for y in range(m-2):
        if array_n[x][y] != array_m[x][y]:
            cnt += 1
            flip(x,y)
if all(a_n==a_m for a_n,a_m in zip(array_n,array_m)):
    print(cnt)
else:
    print(-1)