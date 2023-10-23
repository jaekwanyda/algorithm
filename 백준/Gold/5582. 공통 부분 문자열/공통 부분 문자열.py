import sys
input = sys.stdin.readline
#아이디어: 앞에서 부터 조사 해보자(짧은걸로)
a = input().rstrip()
b = input().rstrip()
if len(a) > len(b):
    a,b = b,a
answer = 0
start = 0
end = 1
n = len(a)
while end <= n:
    while end <= n and start > end:
        end += 1        
    while end <= n and a[start:end] in b:
        end += 1
    answer = max(answer, end-start-1)
    start += 1
print(answer)