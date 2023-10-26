import sys
input = sys.stdin.readline
#아이디어: 정규표현식 사용
import re
n = int(input())
m = re.compile(r'\d+')
answer = []
for _ in range(n):
    a = input().rstrip()
    answer += list(map(int,re.findall(m,a)))
answer.sort()
for a in answer:
    print(a)