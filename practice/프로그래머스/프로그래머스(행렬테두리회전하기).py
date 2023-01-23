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

from collections import deque
def solution(rows, columns, queries):
    answer = []
    array=[[0]*(columns+1) for i in range(rows+1)]
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            array[i][j]=(i-1)*columns+j
    q=deque()
    for querie in queries:
        y1,x1,y2,x2=querie
        for i in range(x1,x2):
            q.append(array[y1][i])
        for i in range(y1,y2):
            q.append(array[i][x2])
        for i in range(x2,x1,-1):
            q.append(array[y2][i])
        for i in range(y2,y1,-1):
            q.append(array[i][x1])
        answer.append(min(q))
        for i in range(x1+1,x2+1):
            array[y1][i]=q.popleft()
        for i in range(y1+1,y2+1):
            array[i][x2]=q.popleft()
        for i in range(x2-1,x1-1,-1):
            array[y2][i]=q.popleft()
        for i in range(y2-1,y1-1,-1):
            array[i][x1]=q.popleft()
    return answer
