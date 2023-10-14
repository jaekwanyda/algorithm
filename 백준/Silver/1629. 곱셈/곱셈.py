import sys
input = sys.stdin.readline
#아이디어: 2진법 처럼 나머지를 이용해 b에 최대한 가까이 가보자
#a,b,c 입력받기
a,b,c = map(int,input().split())
b = format(b,'b') #이진법으로 바꿔주기
cnt = 0
bit_b = []
start = a%c
while cnt < len(b):
    bit_b.append(start)
    start = (start*start)%c
    cnt += 1
answer = 1
for i in range(len(b)):
    if int(b[i]):
        answer *= int(b[i])*bit_b[-i-1]
        answer = answer % c
print(answer)