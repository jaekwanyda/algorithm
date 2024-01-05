import sys
input = sys.stdin.readline
from collections import deque
#아이디어: 모든 이동 경우를 확인하는 것은 4^10 이다. 백트래킹으로 전부 확인해보자
n, m = map(int,input().split())
array = [list(input().rstrip()) for _ in range(n)]
dx = [0,0,-1,1] #left, right, up, down
dy = [-1,1,0,0]
def move(bx,by,rx,ry,direction): #항상 R 먼저 움직이게 하자
    change = False
    if direction == 0: #left
        if by < ry:
            change = True
            bx,by,rx,ry = rx,ry,bx,by
    if direction == 1: #right
        if by > ry:
            change = True
            bx,by,rx,ry = rx,ry,bx,by
    if direction == 2: #up
        if bx < rx:
            change = True
            bx,by,rx,ry = rx,ry,bx,by
    if direction == 3: #down
        if bx > rx:
            change = True
            bx,by,rx,ry = rx,ry,bx,by
    b_possi = False
    r_possi = False

    while array[rx + dx[direction]][ry + dy[direction]] != '#':
        rx += dx[direction]
        ry += dy[direction]
        if array[rx][ry] == 'O':
            if change:
                b_possi = True
            else:
                r_possi = True
            break

    while array[bx + dx[direction]][by + dy[direction]] != '#' and (r_possi or b_possi or bx + dx[direction] != rx or by + dy[direction] != ry):
        bx += dx[direction]
        by += dy[direction]
        if array[bx][by] == 'O':
            if change:
                r_possi = True
            else:
                b_possi = True
            break
    if change:
        bx,by,rx,ry = rx,ry,bx,by
    return bx,by,rx,ry,b_possi,r_possi
def bfs():
    bx,by,rx,ry = -1,-1,-1,-1
    for i in range(n):
        for j in range(m):
            if array[i][j] == 'B':
                bx,by = i,j
            if array[i][j] == 'R':
                rx,ry = i,j
    stack = deque() #B,R의 위치와 이동 횟수, 이동 방향을 담은 stack
    stack.append([[bx,by,rx,ry],0,-1])
    visited = set()
    visited.add((bx,by,rx,ry))
    while stack:
        br_list,num,direction = stack.popleft()
        for i in range(4):
            if i != direction: #이전에 진행했던 방향은 굳이 안봐도 됨
                bx,by,rx,ry,b_possi,r_possi = move(*br_list,i)
                if b_possi:
                    continue
                elif r_possi:
                    print(num+1)
                    return
                else:
                    if num < 9 and not (bx,by,rx,ry) in visited:
                        visited.add((bx,by,rx,ry))
                        stack.append([[bx, by, rx, ry], num+1, i])
    else:
        print(-1)
bfs()