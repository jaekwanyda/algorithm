import sys
input = sys.stdin.readline
#아이디어: stack을 써서 간단하게 해결해보자
input_str = input().rstrip()
answer = []
n = len(input_str)
cnt = 0
while cnt < n:
    if input_str[cnt] == "<":
        while input_str[cnt] != ">":
            answer.append(input_str[cnt])
            cnt += 1
        answer.append(input_str[cnt])
        cnt += 1
    elif input_str[cnt] != ' ':
        stack = []
        while cnt < n and input_str[cnt] != "<" and input_str[cnt] != ' ' :
            stack.append(input_str[cnt])
            cnt += 1
        answer += stack[::-1]
    else:
        answer.append(input_str[cnt])
        cnt += 1
print(''.join(answer))