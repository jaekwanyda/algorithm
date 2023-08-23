import sys
input = sys.stdin.readline
#아이디어: 중앙에서 부터 1,1,2,2,... 개수만큼 이동하고 오른쪽으로 꺾는다.
#n 입력받기
n = int(input())
#찾는 정수 입력받기
target = int(input())
#달팽이 담는 list
array = [[0]*n for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
#중앙 1로 고정하기
num = 1
x = n//2
y = n//2
cnt = 2
direction = 0
array[x][y] = num
while (cnt-1)//2+1 <= n:
    for _ in range(min(cnt//2,n-1)):
        num += 1
        x += dx[direction]
        y += dy[direction]
        array[x][y] = num
    direction = (direction+1)%4
    cnt += 1
for i in range(n):
    if target in array[i]:
        targetx = i
        targety = array[i].index(target)
    print(*array[i])
print(targetx+1, targety+1)