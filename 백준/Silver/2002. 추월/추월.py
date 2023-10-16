import sys
input = sys.stdin.readline
#아이디어: deque를 이용해볼까나
from collections import deque
in_car = deque()
out_car = deque()
n = int(input())
for _ in range(n):
    car = input().rstrip()
    in_car.append(car)
for _ in range(n):
    car = input().rstrip()
    out_car.append(car)
answer = 0
seed = set()
while in_car and out_car:
    ic,oc = in_car.popleft(),out_car.popleft()
    while ic in seed and in_car:
        ic = in_car.popleft()
    seed.add(oc)
    while ic != oc and out_car:
        oc = out_car.popleft()
        answer += 1
        seed.add(oc)
print(answer)