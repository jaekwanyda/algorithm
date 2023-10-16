import sys
input = sys.stdin.readline
#아이디어: union,find 이용해보자 부모 노드 순서는 사전식으로
t = int(input())
for _ in range(t):
    f = int(input())
    friends = {}
    friends_set = {}
    def find(a):
        if friends[a] == a:
            return a
        friends[a] = find(friends[a])
        return friends[a]
    def union(a,b):
        a = find(a)
        b = find(b)
        if a != b:
            friends[b] = a
            friends_set[a].update(friends_set[b])
        # elif b < a:
        #     friends[a] = b
        #     friends_set[b].update(friends_set[a])
    for _ in range(f):
        a,b = input().split()
        if not a in friends:
            friends[a] = a
            friends_set[a] = {a}
        if not b in friends:
            friends[b] = b
            friends_set[b] = {b}
        union(a,b)
        print(len(friends_set[friends[a]]))
