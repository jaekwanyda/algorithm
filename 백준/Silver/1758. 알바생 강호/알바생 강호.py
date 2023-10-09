import sys
input = sys.stdin.readline
#아이디어: 그냥 돈 제일 많이 주는 놈 먼저 받자
#n 입력받기
n = int(input())
#tip 입력받기
tips = []
for _ in range(n):
    tips.append(int(input()))
tips = sorted(tips,reverse=True)
print(sum(max(tip-i,0) for i,tip in enumerate(tips)))