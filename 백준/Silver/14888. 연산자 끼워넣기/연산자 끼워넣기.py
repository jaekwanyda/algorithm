import sys
input = sys.stdin.readline
from collections import deque
#아이디어: 완전 탐색
n = int(input())
nums = list(map(int,input().split()))
opers = list(map(int,input().split()))
maximum = -float('inf')
minimum = float('inf')
stack = [(nums[0],opers,0)] #연산이 진행된 수, 남은 연산들, 진행된 수
end = len(nums) - 1
def operate(a,b,i):
    if i == 0: #덧셈
        return a + b
    if i == 1: #뺄셈
        return a - b
    if i == 2: #곱셈
        return a * b
    if i == 3: #나눗셈
        if a*b<0:
            return (abs(a)//abs(b))*-1
        else:
            return a//b
while stack:
    num,re_opers,cnt = stack.pop()
    for i in range(4):
        if re_opers[i]: #연산이 가능한 경우
            result = operate(num,nums[cnt+1],i)
            if cnt+1 == end:
                maximum = max(maximum,result)
                minimum = min(minimum,result)
            else:
                tmp_opers = re_opers[:]
                tmp_opers[i] -= 1
                stack.append((result,tmp_opers,cnt+1))
print(int(maximum))
print(int(minimum))