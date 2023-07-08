import sys
input = sys.stdin.readline
#아이디어: 그냥 피보나치
#t 입력받기
t = int(input())
#t 크기만큼 피보나치 진행
for _ in range(t):
    #n 입력 받기
    n = int(input())
    pibo = [0]*(n+1)
    pibo[0] = 1
    if n == 0:
        print(1,0)
        continue
    elif n == 1:
        print(0,1)
        continue
    else:
        pibo[1] = 1
        for i in range(2,n+1):
            pibo[i] = pibo[i-1] + pibo[i-2]
        print(pibo[n-2],pibo[n-1])