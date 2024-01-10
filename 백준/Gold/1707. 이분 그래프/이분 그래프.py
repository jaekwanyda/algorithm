import sys
input = sys.stdin.readline
#아이디어: 0,1 로 구분하며 나눠보자
k = int(input())
for _ in range(k):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    binary_possi = True
    binary = [-1]*(v+1)
    binary[1] = True
    stack = [1]
    while stack:
        while stack:
            node = stack.pop()
            node_possi = binary[node]
            for next_node in graph[node]:
                if binary[next_node] == -1:
                    binary[next_node] = not node_possi
                    stack.append(next_node)
                elif binary[next_node] == node_possi:
                    binary_possi = False
                    break
            if not binary_possi:
                break
        if not binary_possi:
            break
        for i in range(1,v+1):
            if binary[i] == -1:
                binary[i] = True
                stack.append(i)
                break
    if binary_possi:
        print("YES")
    else:
        print("NO")            