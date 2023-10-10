import sys
input = sys.stdin.readline
#아이디어: 빨리 도착하는 마을을 더 많이 적재
#마을 수 n, 택배 최대 용량 c 입력
from collections import defaultdict
n,c = map(int,input().split())
#m입력받기
m = int(input())
post = []
for _ in range(m):
    post.append(list(map(int,input().split())))
post = sorted(post,key=lambda x:x[1]) #도착이 빠른 순으로 정렬
stack = [0]*(n+1) #적재된 택배량 저장
answer = 0
for a,b,p in post:
    max_post = min(c-stack[i] for i in range(a,b))
    p = min(max_post,p)
    for i in range(a,b):
        stack[i] += p
    answer += p
print(answer)