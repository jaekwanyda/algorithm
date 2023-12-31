import sys
import copy
import heapq
input = sys.stdin.readline
#아이디어: dp
n = int(input())
nums = [10000001] + list(map(int,input().split()))
m = int(input())
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    #홀수개 펠린드롬
    start,end = i,i
    while 0<start and end<=n:
        if nums[start] == nums[end]:
            dp[start][end] = 1
            start -= 1
            end += 1
        else:
            break
    #짝수개 펠린드롬
    start,end = i,i+1
    while 0<start and end<=n:
        if nums[start] == nums[end]:
            dp[start][end] = 1
            start -= 1
            end += 1
        else:
            break
for _ in range(m):
    s,e = map(int,input().split())
    print(dp[s][e])