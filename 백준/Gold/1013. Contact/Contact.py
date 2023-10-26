import sys
input = sys.stdin.readline
#아이디어: 정규표현식 사용
import re
n = int(input())
m = re.compile(r'(100+1+|01)+')
for _ in range(n):
    a = input().rstrip()
    b = m.fullmatch(a)
    if b :
        print('YES')
    else:
        print('NO')