import sys
input = sys.stdin.readline
#아이디어: 그냥 list를 이용해 구현해보자
while True:
    #명령어 입력받기
    order = input().rstrip()
    if order == 'QUIT':
        break
    order_list = [order]
    if order == 'END':
        order_list.pop()
    else:
        while True:
            order = input().rstrip()
            #입력값이 END면 입력어로 넘어가기
            if order == "END":
                break
            else:
                order_list.append(order)
    #입력어 입력받기
    n = int(input())
    input_list = []
    while True:
        val = input()
        #만약 "" 이 입력되면 하나의 프로그램 입력 종료
        if val == "\n":
            break
        else:
            input_list.append(int(val))
    #이때까지 입력받은 명령어와 입력어를 이용해 출력하기
    for val in input_list:
        #입력어를 담는 list 생성
        error = False
        stack = [val]
        for order in order_list:
            if order[:3] == 'NUM':
                stack.append(int(order[4:]))
            #숫자가 부족해서 연산을 수행할 수 없을 때 프로그램 오류
            elif len(stack) == 0:
                 error = True
                 break
            elif order == 'INV':
                stack[-1] = -1*stack[-1]
            elif order == 'POP':
                stack.pop()
            elif order == 'DUP':
                stack.append(stack[-1])
            #숫자가 두개 이상 필요한 연산에서는 2개 이하일 때 프로그램 오류
            elif len(stack) == 1:
                error = True
                break
            elif order == 'SWP':
                first = stack.pop()
                second = stack.pop()
                stack.append(first)
                stack.append(second)
            elif order == 'ADD':
                first = stack.pop()
                new_first = stack[-1] + first
                #연산결과가 10**9 이상인 경우 오류
                if abs(new_first) > 1e9:
                    error = True
                    break
                else:
                    stack[-1] = new_first
            elif order == 'SUB':
                first = stack.pop()
                new_first = stack[-1] - first
                #연산결과가 10**9 이상인 경우 오류
                if abs(new_first) > 1e9:
                    error = True
                    break
                else:
                    stack[-1] = new_first
            elif order == 'MUL':
                first = stack.pop()
                new_first = stack[-1] * first
                #연산결과가 10**9 이상인 경우 오류
                if abs(new_first) > 1e9:
                    error = True
                    break
                else:
                    stack[-1] = new_first
            #0으로 나누는 경우도 오류
            elif stack[-1] == 0:
                error = True
                break
            elif order == 'DIV':
                first = stack.pop()
                new_first = abs(stack[-1]) // abs(first)
                if stack[-1] * first < 0:
                    new_first *= -1
                stack[-1] = new_first
            elif order == 'MOD':
                first = stack.pop()
                new_first = abs(stack[-1]) % abs(first)
                #나머지의 부호는 피제수의 부호
                if new_first * stack[-1] < 0:
                    new_first *= -1
                stack[-1] = new_first
        #모든 과정을 마치고 stack의 수가 1인 경우 출력, 아닌 경우 ERROR 출력
        if len(stack) != 1 or error:
            print('ERROR')
        else:
            print(stack[-1])
    print('')