import sys
input = sys.stdin.readline
#아이디어: 기회는 한번. 두번은 없다.
from collections import deque
t = int(input())
for _ in range(t):
    tmp = input().rstrip()
    if tmp == tmp[::-1]:
        print(0)
        continue
    tmp = deque(tmp)
    cnt = 0
    while len(tmp) >= 2 and cnt < 2:
        a,b = tmp.popleft(),tmp.pop()
        if a == b:
            continue
        else:
            tmp = list(tmp)
            if tmp + [b] == [b] + tmp[::-1]:
                print(1)
            elif [a] + tmp == tmp[::-1] + [a]:
                print(1)
            else:
                print(2)
            break