import sys
input = sys.stdin.readline
#아이디어: 완전 탐색을 해보자. d1이 늘어났을 때, d2가 늘어났을 때, 둘 다 늘어났을 때 차이가 줄어든다면 진행하자
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
answer = float('inf')
def check(x,y,d1,d2):
    global answer
    x1,x2,x3,x4,x5 = 0,0,0,0,0 #선거구 확인
    if 0<=x-d1 and x+d2<n and y+d1+d2<n: #선거구 크기가 가능한 경우
        for i in range(n):
            for j in range(n):
                if x-d1<=i<=x+d2:
                    if i<=x:
                        start = x+y-i
                    else:
                        start = -x+y+i
                    if i<=x-d1+d2:
                        end = -x+y+2*d1+i
                    else:
                        end = x+y+2*d2-i
                    if start<=end and start<=j<=end:
                        x5 += array[i][j]
                        continue
                if i<x and j<=y+d1:
                    x1 += array[i][j]
                elif i<=x-d1+d2 and j>y+d1:
                    x2 += array[i][j]
                elif i>=x and j<y+d2:
                    x3 += array[i][j]
                else:
                    x4 += array[i][j]
        answer = min(answer,max(x1,x2,x3,x4,x5)-min(x1,x2,x3,x4,x5))
for x in range(n):
    for y in range(n):
        for d1 in range(1,n):
            for d2 in range(1,n):
                check(x,y,d1,d2)
print(answer)