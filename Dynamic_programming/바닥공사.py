# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
#아코테 다이나믹 연습 4
#N입력받기
n=int(input())
#이문제도 2가지 경우로 나눌 수 있다.
#1) 맨 마지막을 2X1 타일로 채우기 => dp[i-1] 2) 맨 마지막을 2X2 or 1X2 2개로 채우기(경우의 수 2) => 2*dp[i-2]
dp=[0]*(n+1)
dp[1]=1
dp[2]=3

for i in range(3,n+1):
    dp[i]=(dp[i-1]+2*dp[i-2])%796796
    
print(dp[n])
# -


