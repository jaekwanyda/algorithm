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
#이코테 실전 19(백준 14888)
#아이디어: 중복순열을 이용해 가능한 사칙연산의 모든 가능성을 센다면 가능할 것 같다.
n=int(input())
array=list(map(int,input().split()))
plus,minus,multi,div=map(int,input().split()) #사칙연산 갯수 입력받기
max_val=-987654321
min_val=987654321
#dfs로 모든 가능성 세기
def dfs(i,now): #dfs를 사용한 횟수와 그 시점의 계산 값을 보내주기:
    global max_val,min_val,plus,minus,multi,div
    if i==n:
        max_val=max(max_val,now)
        min_val=min(min_val,now)
    else:
        if plus>0:
            plus-=1
            dfs(i+1,now+array[i])
            plus+=1
        if minus>0:
            minus-=1
            dfs(i+1,now-array[i])
            minus+=1
        if multi>0:
            multi-=1
            dfs(i+1,now*array[i])
            multi+=1
        if div>0:
            div-=1
            dfs(i+1,int(now/array[i]))
            div+=1
            
dfs(1,array[0])
print(max_val)
print(min_val)
# -


