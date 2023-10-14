import sys
input = sys.stdin.readline
#아이디어: 또다시 이진법으로 구현해보자
n,b = map(int,input().split())
b = format(b,'b')
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
def multi_mat(a,b):
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = sum(a[i][k]*b[k][j] for k in range(n))%1000
    return c
cnt = 0
array_b = []
while cnt<len(b):
    array_b.append(array)
    array = multi_mat(array,array)
    cnt += 1
answer = [[0]*n for _ in range(n)]
for i in range(n):
    answer[i][i] = 1
for i in range(len(b)):
    if int(b[i]):
        answer = multi_mat(answer,array_b[-i-1])
for i in range(n):
    print(*answer[i])