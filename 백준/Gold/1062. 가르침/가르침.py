import sys
input = sys.stdin.readline
#아이디어: 그냥 26Ck를 해도 얼마 안나올 것 같기는 하다. 
from itertools import combinations
n,k = map(int,input().split())
stack = []
for _ in range(n):
    s = set(list(input().rstrip()))
    stack.append(s)
if k<5: #적어도 a,c,i,n,t 는 포함해야 한다.
    print(0)
else:
    total = set()
    for s in stack:
        total = total.union(s)
    total -= {'a','c','i','n','t'}
    answer = 0
    if not total:
        for s in stack:
            if s.issubset({'a','c','i','n','t'}):
                answer += 1
        print(answer)
    else:
        for new_comb in combinations(total,min(k-5,len(total))):
            new_comb = set(new_comb).union({'a','c','i','n','t'})
            cnt = 0
            for s in stack:
                if s.issubset(new_comb):
                    cnt += 1
            answer = max(answer, cnt)
        print(answer)