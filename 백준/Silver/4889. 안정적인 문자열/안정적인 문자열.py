import sys
input = sys.stdin.readline
#아이디어: 그냥 여는 괄호, 닫는 괄호 개수 세서 차이 만큼 출력해주면 될듯 + 닫힌 괄호가 앞에 있을 경우 바꿔주자
n = 1
while True:
    input_s = list(input())
    input_s.pop()
    if '-' in input_s:
        break
    change = 0
    open = 0; close = 0
    for i in range(len(input_s)):
        if input_s[i] == '{':
            open += 1
        else:
            close += 1
        #만약 앞에서 닫는 괄호가 더 많은 경우 여는 괄호로 바꿔준다.
        if close > open:
            change += 1
            close -= 1
            open += 1
    #이렇게 여는 괄호와 닫는 괄호 개수를 다 세주면 그 차이의 반절만큼 바꿔주면 된다
    print(f'{n}. {abs((close-open)//2)+change}')
    n += 1
