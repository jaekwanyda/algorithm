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
#아코테 정렬 연습 2
#N 입력받기
n=int(input())
#N개의 정수 입력받기
array=[]
for i in range(n):
    array.append(int(input()))
    
array=sorted(array,reverse=True) #라이브러리 이용

for i in array:
    print(i,end=' ')
# -


