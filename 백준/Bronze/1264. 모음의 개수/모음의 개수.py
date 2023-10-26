import sys
input = sys.stdin.readline
#아이디어: 정규표현식 사용
import re
m = re.compile(r'[a|e|i|o|u|A|E|I|O|U]')
while True:
    s = input().rstrip()
    if s =='#':
        break
    print(len(re.findall(m,s)))
