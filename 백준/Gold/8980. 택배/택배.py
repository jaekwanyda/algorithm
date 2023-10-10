import sys
input = sys.stdin.readline
#아이디어: 빨리 도착하는 마을을 더 많이 적재? 더 많은 택배를 보내는 마을을 더 많이 적재?
#마을 수 n, 택배 최대 용량 c 입력
from collections import defaultdict
n,c = map(int,input().split())
#m입력받기
m = int(input())
post = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,cost = map(int,input().split())
    post[a].append([b,cost])
for i in range(1,n+1):
    post[i] = sorted(post[i])
p_dict = defaultdict(int)
tmp = 0 #현재 담고 있는 총 택배 수
answer = 0
for i in range(1,n+1): #각각의 마을에 대해서
    if p_dict[i]: #도착 택배 처리
        tmp -= p_dict[i]
        answer += p_dict[i]
        p_dict[i] = 0
    for j,p in post[i]: #도착 마을과 택배량
        if tmp+p<=c:
            p_dict[j] += p
            tmp += p
        else:
            p_dict[j] += c-tmp
            tmp = c
            break
print(answer)