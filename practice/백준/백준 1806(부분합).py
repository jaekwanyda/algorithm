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

#아이디어:2포인터 식으로 하면 될 것 같다.
#n,s입력받기
n,s=map(int,input().split())
array=list(map(int,input().split()))
start_index=0
end_index=1
dp=[0]*(n+1)
#부분합 구하기
for i in range(1,n+1):
    dp[i]=dp[i-1]+array[i-1]
possible=[]
while end_index<n+1:
    a=dp[end_index]-dp[start_index]
    if a>=s: #큰 경우엔 리스트에 더해주고 start_index 더해주기
        possible.append(end_index-start_index)
        start_index+=1
    else:#작은 경우엔 end_index더해주기
        end_index+=1
if len(possible)==0:
    print(0)
else:
    print(min(possible))
        


