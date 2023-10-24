import sys
input = sys.stdin.readline
#아이디어: T의 끝 글자를 보면 이 전의 글자를 파악할 수 있다.
s = input().rstrip()
t = input().rstrip()
len_s = len(s)
while len(t) > len_s:
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]
if s == t:
    print(1)
else:
    print(0)