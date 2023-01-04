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
#아코테 다이나믹 연습 5
#N, M 입력받기
n,m=map(int,input().split())
array=[int(input()) for _ in range(n)] #column으로 각각의 값 입력받기
#dp 테이블 생성(이번에는 아닌 경우에 -1로 초기화 해주어야 해서 나올 수 있는 가장 큰 수 10000보다 1큰 10001로 초기화)
dp=[0]*(m+1)

for i in range(1,m+1):
    #가능한 경우를 추가할 리스트
    a=[]
    #리스트에 존재하는 각각의 값들을 이용
    for j in array:
        if i-j==0:#계산이 가능할 때
            a.append(1)
        if i-j>0 and dp[i-j]>0: #j원을 뺐을 때 가능한 계산이 있다면 추가
            a.append(dp[i-j]+1)
    if len(a)==0:
        dp[i]=-1
    else:
        dp[i]=min(a)

print(dp[m])
# -


