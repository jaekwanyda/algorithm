import sys
input = sys.stdin.readline
#아이디어: 끝에서 부터 빼면서 커질 수 있으면 바로 끝내자
t = int(input())
for _ in range(t):
    ch = list(input().rstrip())
    origin = ch[:]
    stack = []
    while ch:
        a = ord(ch.pop())
        stack = sorted(stack, key = lambda x:-x)    
        if stack and stack[0] > a:
            cnt = 0
            while cnt < len(stack) and stack[cnt] > a:
                cnt += 1
            stack = [stack.pop(cnt-1)] + sorted([a]+stack)
            ch += [chr(s) for s in stack]
            print(''.join(ch))
            stack = []
            break
        else:
            stack.append(a)
    if stack:
        print(''.join(origin))