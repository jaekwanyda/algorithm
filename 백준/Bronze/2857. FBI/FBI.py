import sys
input = sys.stdin.readline
#아이디어: 정규표현식 사용
import re
m = re.compile(r'FBI')
answer = []
for i in range(5):
    agent = input().rstrip()
    if m.findall(agent):
        answer.append(i+1)
if answer:
    print(*answer)
else:
    print('HE GOT AWAY!')