import sys
input = sys.stdin.readline
#아이디어: 그냥 최대한 큰 수끼리 곱해주자. 음수인 경우만 신경 써보자
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()
positive = []
nagative = []
for a in array:
    if a > 0:
        positive.append(a)
    elif a < 0:
        nagative.append(a)
nagative.reverse()
answer = 0
while len(positive) >= 2:
    a,b = positive.pop(),positive.pop() 
    if a != 1 and b != 1:
        answer += a*b
    else:
        answer += (a+b)
if positive:
    answer += positive[0]
while len(nagative) >= 2:
    a,b = nagative.pop(),nagative.pop()
    answer += a*b
if nagative:
    if 0 not in array:
        answer += nagative[0]
print(answer)