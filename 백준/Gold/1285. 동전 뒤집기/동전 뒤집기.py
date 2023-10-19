import sys
input = sys.stdin.readline
#아이디어: 한 열을 굳이 2번 바꿀 이유는 없다. 순서도 상관이 없다. 그렇기에 n개의 열을 바꿀지 말지 정하고 바뀐 동전 맵에서 뒷면이 줄어드는 행만 뒤집어주자
n = int(input())
coins = []
coin_dict = {'H':'0','T':'1'}
for _ in range(n):
    coins.append(input().rstrip())
#동전 정보들 2진법으로 변환해주기
for i,coin in enumerate(coins):
    tmp = '0b'
    for c in coin:
        tmp += coin_dict[c]
    coins[i] = int(tmp,2)
# 결과값을 저장할 변수
answer = float('inf')
flip_coins = [int(coins[i])^(int('0b'+'1'*n,2)) for i in range(n)]
original = coins[:]
# 가능한 각 동전 뒷면을 고려하여 결정
for i in range(1 << n):  # 모든 가능한 결정을 확인
    #동전 뒤집어주기
    for j in range(n):
        if i & (1 << j):  # 동전을 뒤집는 결정인 경우
            coins[j] = flip_coins[j]
    #세로로 T 개수 세주기. 만약 n 보다 많으면 뒤집어서 줄여주기
    total_flips = 0  # 현재 결정에서의 뒷면 수
    start = 1
    for j in range(n):
        flips = 0
        for k in range(n):
            if start & coins[k]:
                flips += 1
        total_flips += min(flips,n-flips)
        start = start << 1
    answer = min(answer, total_flips)
    coins = original[:]
print(answer)