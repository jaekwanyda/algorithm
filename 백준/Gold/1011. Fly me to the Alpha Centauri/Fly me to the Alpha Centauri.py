import sys
input = sys.stdin.readline
#아이디어: dp로 해결하자
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    distance = y-x
    if distance < 4:
        print(distance)
        continue
    root_distance = int(distance**(1/2))
    if distance == root_distance**2:
        print(2*root_distance-1)
    elif distance <= root_distance*(root_distance+1):
        print(2*root_distance)
    else:
        print(2*root_distance+1)