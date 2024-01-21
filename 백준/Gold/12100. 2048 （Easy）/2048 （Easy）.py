import sys
input = sys.stdin.readline
from collections import deque
import copy
#아이디어: 완전탐색(4^5) 만큼 확인하면 됨
n = int(input())
list_2048 = [list(map(int,input().split())) for _ in range(n)]
answer = list_2048[0][0] #n == 1인 경우
def up(array):
    global answer
    for i in range(n):
        column = deque()
        for j in range(n):
            if array[j][i] != 0:
                column.append(array[j][i])
        if not column:
            continue
        answer = max(answer,max(column))
        result = []
        current_num = column.popleft()
        while column:
            num = column.popleft()
            if current_num == num:
                result.append(num*2)
                current_num = 0
            elif current_num != 0:
                result.append(current_num)
                current_num = num
            else:
                current_num = num
        result.append(current_num)
        while len(result) < n:
            result.append(0)
        for j in range(n):
            array[j][i] = result[j]
    return array
def down(array):
    global answer
    for i in range(n):
        column = deque()
        for j in range(n):
            if array[j][i] != 0:
                column.append(array[j][i])
        column.reverse()
        if not column:
            continue
        answer = max(answer,max(column))
        result = []
        current_num = column.popleft()
        while column:
            num = column.popleft()
            if current_num == num:
                result.append(num*2)
                current_num = 0
            elif current_num != 0:
                result.append(current_num)
                current_num = num
            else:
                current_num = num
        result.append(current_num)
        while len(result) < n:
            result.append(0)
        result.reverse()
        for j in range(n):
            array[j][i] = result[j]
    return array
def left(array):
    global answer
    for i in range(n):
        row = deque()
        for j in range(n):
            if array[i][j] != 0:
                row.append(array[i][j])
        result = []
        if not row:
            continue
        answer = max(answer,max(row))
        current_num = row.popleft()
        while row:
            num = row.popleft()
            if current_num == num:
                result.append(num*2)
                current_num = 0
            elif current_num != 0:
                result.append(current_num)
                current_num = num
            else:
                current_num = num
        result.append(current_num)
        while len(result) < n:
            result.append(0)
        for j in range(n):
            array[i][j] = result[j]
    return array
def right(array):
    global answer
    for i in range(n):
        row = deque()
        for j in range(n):
            if array[i][j] != 0:
                row.append(array[i][j])
        row.reverse()
        if not row:
            continue
        answer = max(answer,max(row))
        result = []
        current_num = row.popleft()
        while row:
            num = row.popleft()
            if current_num == num:
                result.append(num*2)
                current_num = 0
            elif current_num != 0:
                result.append(current_num)
                current_num = num
            else:
                current_num = num
        result.append(current_num)
        while len(result) < n:
            result.append(0)
        result.reverse()
        for j in range(n):
            array[i][j] = result[j]
    return array
def dfs(array,cnt):
    if n == 1:
        return
    if cnt < 6:
        up_array = up(copy.deepcopy(array))
        dfs(up_array,cnt+1)
        down_array = down(copy.deepcopy(array))
        dfs(down_array,cnt+1)
        left_array = left(copy.deepcopy(array))
        dfs(left_array,cnt+1)
        right_array = right(copy.deepcopy(array))
        dfs(right_array,cnt+1)
dfs(list_2048,0)
print(answer)
#왼아왼위왼