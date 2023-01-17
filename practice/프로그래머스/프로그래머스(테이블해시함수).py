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

#배운점: 이때까지 제곱쓸일이 없어서 ^의 기능을 망각하고 있었는데 ^는 bitwise XOR을 할때 사용하는 것이다.
def solution(data, col, row_begin, row_end):
    data=sorted(data,key= lambda x:(x[col-1],-x[0]))
    v=0
    for i in data[row_begin-1]:
        v+= (i%row_begin)
    for i in range(row_begin,row_end):
        s=0
        for j in data[i]:
            s+=(j%(i+1))
        v=v^s
        print(v)
    return v
