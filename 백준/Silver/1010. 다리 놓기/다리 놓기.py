import sys
input = sys.stdin.readline
#아이디어: 그냥 combination
import math
#t 입력받기
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    print(math.comb(b,a))