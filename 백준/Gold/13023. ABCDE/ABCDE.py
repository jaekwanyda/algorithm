import sys
input = sys.stdin.readline
#아이디어: dfs를 하면서 체크해보자
n,m = map(int,input().split())
friends = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)
stack = [[i] for i in range(n)]
while stack:
    s = stack.pop()
    if len(s) == 5:
        print(1)
        break
    start = s[-1]
    for f in friends[start]:
        if f not in s:
            stack.append(s+[f])
else:
    print(0)