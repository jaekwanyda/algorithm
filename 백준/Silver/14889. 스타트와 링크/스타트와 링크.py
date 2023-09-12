import sys
input = sys.stdin.readline
#아이디어: 조합 + 전체 시너지 합을 미리 구하면 시간을 좀 단축할 수 있을 것 같다
from itertools import combinations
#n입력받기
n = int(input())
#시너지 입력받기
array = [list(map(int,input().split())) for _ in range(n)]
total = sum(sum(a) for a in array)
min_val = 99999999
for team1 in combinations(range(n),n//2):
    team = set(range(n))
    val1 = 0
    for x in team1:
        for y in team1:
            val1 += array[x][y]
    team2 = team - set(team1)
    val2 = 0
    for x in team2:
        for y in team2:
            val2 += array[x][y]
    val = abs(val1-val2)
    min_val = min(min_val,val)
print(min_val)