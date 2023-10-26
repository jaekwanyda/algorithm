import sys
input = sys.stdin.readline
#아이디어: 정규표현식 사용
import re
a = input().rstrip()
b = input().rstrip()
m = re.compile(b)
print(len(re.findall(m,a)))