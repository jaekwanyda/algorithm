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
#이코테 실전 32(백준 1932)
#아이디어: 위의 삼각형에서 두 개 값 중 최대인 것을 더해 새로운 삼각형을 만들면 될 것 같다.
#n 입력받기
n=int(input())
dp=[[0]*n for _ in range(n)]#dp테이블 형성
#list로 입력받기
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))
#dp 테이블에 추가
dp[0][0]=array[0][0]
for i in range(1,n):
    for j in range(i+1):
        if j==0:
            dp[i][j]=dp[i-1][j]+array[i][j] #맨 왼쪽의 경우 위의 값 그대로
        elif j==i:
            dp[i][j]=dp[i-1][j-1]+array[i][j] #맨 오른쪽의 경우 왼쪽 위 값 그대로
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+array[i][j]

print(max(dp[n-1]))
# -


