import sys
input = sys.stdin.readline
#아이디어: 직접 구해보자
#p 입력받기
p = int(input())
for i in range(p):
    _,k = map(int,input().split())
    cnt = 2
    a,b = 1,1
    while True:
        if a == 1 and b == 0:
            break
        a,b = b,(a+b)%k
        cnt += 1       
    print(i+1, cnt)