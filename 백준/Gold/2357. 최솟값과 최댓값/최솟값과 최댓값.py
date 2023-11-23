import sys
input = sys.stdin.readline
#아이디어: 세그먼트 트리 문제이다
n,m = map(int,input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))
length = 1
while True:
    if length >= len(nums):
        break
    length *= 2
max_segment = [0]*(length*2)
min_segment = [float('inf')]*(length*2)
def init(node, start, end, oper): 
    if start == end :
        if oper == 'min':
            min_segment[node] = nums[start]
        else:
            max_segment[node] = nums[start]
        return min_segment[node]
    else :
        if oper == 'min':
            min_segment[node] = min(init(node*2, start, (start+end)//2,'min'), init(node*2+1, (start+end)//2+1, end,'min'))
            return min_segment[node]
        else:
            max_segment[node] = max(init(node*2, start, (start+end)//2,'max'), init(node*2+1, (start+end)//2+1, end,'max'))
            return max_segment[node]
def suboper(node, start, end, left, right,oper) :
    if left > end or right < start :
        if oper == 'min':
            return float('inf')
        else:
            return 0
    if left <= start and end <= right :
        if oper == 'min':
            return min_segment[node]
        else:
            return max_segment[node]
    if oper == 'min':
        return min(suboper(node*2, start, (start+end)//2, left, right,oper),suboper(node*2 + 1, (start+end)//2+1, end, left, right,oper))
    else:
        return max(suboper(node*2, start, (start+end)//2, left, right,oper),suboper(node*2 + 1, (start+end)//2+1, end, left, right,oper))
init(1,0,n-1,'min')
init(1,0,n-1,'max')
for _ in range(m):
    a,b = map(int,input().split())
    print(suboper(1, 0, n-1 ,a-1, b-1,'min'),suboper(1, 0, n-1 ,a-1, b-1,'max'))