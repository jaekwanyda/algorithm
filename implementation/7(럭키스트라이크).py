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
#이코테 기출 7
#아이디어: 단순한 구현문제이다. 입력 리스트를 반으로 나눈뒤 각각의 합을 비교하면 된다.
array=list(map(int,input()))

a=len(array) #array의 길이 저장
b=int(a*0.5)
left_list=array[0:b]
right_list=array[b:]
if sum(left_list)==sum(right_list): #각 리스트의 합이 같을 때 출력
    print('LUCKY')
else:
    print('READY')
# -


