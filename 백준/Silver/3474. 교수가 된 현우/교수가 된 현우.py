import sys
input = sys.stdin.readline
#아이디어: 2의 배수와 5의 배수를 세주면 될듯? 엥간하면 5만 세면 됨
#t입력받기
t = int(input())
for _ in range(t):
    a = int(input())
    answer = 0
    while a>0:
        a = a//5
        answer += a
        
    print(answer)