import sys
input = sys.stdin.readline
#아이디어: 정규표현식 사용
import re
m = re.compile(r'(100+1+|01)+')
a = input().rstrip()
b = m.fullmatch(a)
if b :
    print('SUBMARINE')
else:
    print('NOISE')