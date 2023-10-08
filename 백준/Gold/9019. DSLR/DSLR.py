import sys
input = sys.stdin.readline
#아이디어:bfs를 이용해서 가장 짧게 완성되었을 경우를 출력해주자
from collections import deque
#t 입력받기
t = int(input())
#D 연산
def d(n):
    return 2*n % 10000
#S 연산
def s(n):
    if n == 0:
        return 9999
    return n-1
#L 연산
def l(n):
    return (10*n)%10000 + n//1000
#R 연산
def r(n):
    return (n%10)*1000 + n//10
for _ in range(t):
    a,b = map(int,input().split())
    q = deque()
    visited = {a}
    q.append((a,''))
    while q:
        now, oper = q.popleft()
        if now == b:
            print(oper)
            break
        d_n,s_n,l_n,r_n = d(now),s(now),l(now),r(now)
        if not d_n in visited:
            q.append((d_n,oper+'D'))
            visited.add(d_n)
        if not s_n in visited:
            q.append((s_n,oper+'S'))
            visited.add(s_n)
        if not l_n in visited:
            q.append((l_n,oper+'L'))
            visited.add(l_n)
        if not r_n in visited:
            q.append((r_n,oper+'R'))
            visited.add(r_n)