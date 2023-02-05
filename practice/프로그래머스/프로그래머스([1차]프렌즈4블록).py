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

#아이디어: 최대 900개의 블록이니 각각의 블록 별로 가능한지 확인
import copy
def solution(m, n, board):
    result=[[] for _ in range(n)] #세로 방향으로 저장할 리스트 생성
    answer=0
    for i in range(n):
        for j in range(m):
            result[i].append([board[j][i],1]) #삭제 여부까지 추가
    dx=[0,1,1];dy=[1,0,1]
    while True:
        remove=[]
        for i in range(n-1):
            for j in range(m-1):
                if result[i][j][1]==1:#삭제 안되었을 경우
                    k=result[i][j][0];possi=True #삭제 가능 여부
                    for p in range(3):
                        #일치하지 않거나 삭제된 않은 블럭에 대해 확인
                        if result[i+dx[p]][j+dy[p]][0]!=result[i][j][0] or result[i+dx[p]][j+dy[p]][1]==0:
                            possi=False
                            break
                    if possi:
                        remove.append([i,j])
                        for p in range(3):
                            remove.append([i+dx[p],j+dy[p]])
        #삭제 리스트 대로 삭제해주기
        for i,j in remove:
            result[i][j][1]=0
        array=[]
        for r in result:
            array.append(sorted(r,key=lambda x:x[1])) #삭제된 것들 앞으로 보내게 정렬
        if array==result:
            break
        else:
            result=copy.deepcopy(array)
    #삭제된 것들 개수 세기
    for r in result:
        for x,re in r:
            if re==0:
                answer+=1
                    
    return answer
