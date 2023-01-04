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
#아코테 다이나믹 연습 3
#식량창고 갯수 N 입력받기
n=int(input())
#식량창고 array 입력받기
array=list(map(int,input().split()))

#상향식 풀이를 위해 dp 테이블 형성
dp=[0]*101 #최대 식량창고 갯수는 100
dp[1]=array[1] #창고가 1개일 때는 확정
for i in range(2,n+1):
    #이 문제는 2가지 경우로 나눌 수 있다.
    # 1. i번째 창고를 포함할 때 =>dp[i-2]+array[i] 2) 안할 때 => dp[i]
    dp[i]=max(dp[i-1],dp[i-2]+array[i-1]) #array의 index와 dp의 index는 1씩 차이난다. 
    
print(dp[len(array)])
# -


