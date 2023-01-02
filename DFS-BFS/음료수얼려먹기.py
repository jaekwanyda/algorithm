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

#N,M 값 입력받기
n,m=map(int,input().split())
#얼음 틀 형태 입력받기
array=[list(map(int,input().split())) for _ in range(n)]
#물을 첫 노드부터 붓는다고 생각하자. 이미 부어진 부분에 방문처리를 하면 총 얼음 개수를 구할 수 있을 것이다.
#전부 탐색해야 하므로 DFS가 적절하다. 이유와 근거는 풀면서 더 찾아보자
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #아직 방문 전이라면 방문처리
    if array[x][y]==0:
        array[x][y]=1
        #인접한 네개의 노드에도 dfs사용해서 처리해주기
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)
