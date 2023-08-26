import sys
input = sys.stdin.readline
#아이디어: deque를 써서 rotate를 사용해보자
from collections import deque
#N,M,R 입력받기
n,m,r = map(int,input().split())
#배열 입력 받기
array = [list(map(int,input().split())) for _ in range(n)]
#배열 돌려주기
start = (0,0)
end = (n-1,m-1)
q = deque()
while start[0] < end[0] and  start[1] < end[1]:
    start_row = start[0]
    end_row = end[0]
    start_column = start[1]
    end_column = end[1]
    #1번째 줄 넣어주기
    for i in range(start_row,end_row):
        q.append(array[i][start_column])
    for i in range(start_column,end_column):
        q.append(array[end_row][i])
    for i in range(end_row,start_row,-1):
        q.append(array[i][end_column])
    for i in range(end_column,start_column,-1):
        q.append(array[start_row][i])
    q.rotate(r)
    for i in range(start_row,end_row):
        array[i][start_column] = q.popleft()
    for i in range(start_column,end_column):
        array[end_row][i] = q.popleft()
    for i in range(end_row,start_row,-1):
        array[i][end_column] = q.popleft()
    for i in range(end_column,start_column,-1):
        array[start_row][i] = q.popleft()
    start = (start[0] + 1, start[1] + 1)
    end = (end[0] - 1, end[1] - 1)

for i in range(n):
    print(*array[i])
