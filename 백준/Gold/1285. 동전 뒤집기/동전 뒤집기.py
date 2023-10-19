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
#바꿔주는 함수
answer = float('inf')
ones= int('0b' + '1'*n,2)
reverse_coins = [coins[depth]^ones for depth in range(n)]
original = coins[:]
def dfs(depth):
    global answer
    #전부 바꿨으면 결과값 기록
    if depth == n:
        s = 0
        start = 0b1
        for _ in range(n):
            tmp = 0
            for i in range(n):
                if coins[i] & start:
                    tmp += 1
            tmp = min(tmp,n-tmp)
            s += tmp
            start = start << 1
        answer = min(answer,s)
    else:
        coins[depth] = reverse_coins[depth] #뒤집어주기
        dfs(depth+1)
        coins[depth] = original[depth] #다시 돌려주기
        dfs(depth+1)
dfs(0)
print(answer)