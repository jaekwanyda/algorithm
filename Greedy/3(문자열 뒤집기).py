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
#이코테 실전 3(백준 1439)
#아이디어: 0 덩어리와 1덩어리 수를 구해서 더 작은 덩어리를 뒤집자
#문자열 입력받기
array=list(input())
zero_one=[0,0] #덩어리 수 기록
zero_one[int(array[0])]+=1 #첫번째 덩어리 등록
for i in range(1,len(array)):
    if array[i]!=array[i-1]: #다를 경우 array[i]의 값의 덩어리 수 추가
        zero_one[int(array[i])]+=1
        
print(min(zero_one))
# -

zero_one


