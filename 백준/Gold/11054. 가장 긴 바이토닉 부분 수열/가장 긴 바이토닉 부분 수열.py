import sys
input = sys.stdin.readline
from collections import defaultdict
#아이디어: 증가 DP와 감소 DP를 이용해 증감 DP를 짜보자
n = int(input())
arr = list(map(int,input().split()))
n = len(arr)
lis_dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and lis_dp[i] < lis_dp[j] + 1:
            lis_dp[i] = lis_dp[j] + 1
n = len(arr)
lds_dp = [1] * n
for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[i] > arr[j] and lds_dp[i] < lds_dp[j] + 1:
            lds_dp[i] = lds_dp[j] + 1
max_length = 0
for i in range(n):
    max_length = max(max_length, lis_dp[i] + lds_dp[i] - 1)
print(max_length)
