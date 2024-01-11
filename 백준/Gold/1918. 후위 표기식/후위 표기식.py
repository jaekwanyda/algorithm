# import sys
# input = sys.stdin.readline
#아이디어: 우선순위(괄호 => 곱셈,나눗셈 => 덧셈,뺄셈) 대로 해결해보자
def dfs(str):
    while '(' in str: #괄호 먼저 처리
        cnt = 0
        start = str.find('(')
        for i in range(len(str)):
            if str[i] == '(':
                cnt += 1
            elif str[i] == ')':
                end = i
                cnt -= 1
                if cnt == 0:
                    str = str.replace(str[start:end+1], dfs(str[start+1:end]))
                    break
    while '*' in str or '/' in str: #'*'은 3으로 '/'은 4로 치환
        for i in range(len(str)):
            if str[i] == '*' or str[i] == '/':
                if str[i] == '*':
                    oper = '3'
                else:
                    oper = '4'
                start = i-1
                end = i+1
                while start >= 0 and str[start].isalnum():
                    start -= 1
                while end < len(str) and str[end].isalnum():
                    end += 1
                start += 1
                end -= 1
                str = str.replace(str[start:end+1], str[start:i] + str[i+1:end+1] + oper)
                break
    while '+' in str or '-' in str:
        for i in range(len(str)):
            if str[i] == '+' or str[i] == '-':
                if str[i] == '+':
                    oper = '1'
                else:
                    oper = '2'
                start = i-1
                end = i+1
                while start >= 0 and str[start].isalnum():
                    start -= 1
                while end < len(str) and str[end].isalnum():
                    end += 1
                start += 1
                end -= 1
                str = str.replace(str[start:end+1], str[start:i] + str[i+1:end+1] + oper)
                break
    return str
notation = input()
postfix_notation = dfs(notation)
postfix_notation = postfix_notation.replace('1','+')
postfix_notation = postfix_notation.replace('2','-')
postfix_notation = postfix_notation.replace('3','*')
postfix_notation = postfix_notation.replace('4','/')
print(postfix_notation)