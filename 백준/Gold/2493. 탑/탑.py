import sys
input = sys.stdin.readline
from collections import deque
#아이디어: 2포인터?
n = int(input())
array = list(map(int,input().split()))
stack = [(array[0],0)]
answer = [0]*n
for i in range(1,n):
    while stack and stack[-1][0] < array[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1][1] + 1
    stack.append((array[i],i))
print(*answer)