import sys
input = sys.stdin.readline
#아이디어: 그냥 피보나치
#n 입력받기
n = int(input())
#n 크기만큼 피보나치 진행
pibo = [0]*(n+1)
pibo[0] = 1;pibo[1] = 1
for i in range(2,n+1):
    pibo[i] = (pibo[i-2] + pibo[i-1])%10007
print(pibo[n])