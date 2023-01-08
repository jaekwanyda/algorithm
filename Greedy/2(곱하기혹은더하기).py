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

#이코테 기출 2
#아이디어: 단순히 0,1일 때나 앞의 수가 0일때만 더하고 나머지는 곱하는게 나을거라 생각
#숫자 입력받기
array=list(map(int,input())) #띄어쓰기 안되게 입력받은거 처음에 놓침(틀렸던 부분!)
a=0
#연산 실행하기
for i in array:
    if a==0: #이전 값이 0일 때는 더하는게 최선
        a+=i
    elif i==0 or i==1: # 연산해줄 값이 0이나 1일 때는 더하는게 최선
        a+=i
    else: # 나머지 수는 다 곱해주는게 최선
        a*=i
print(a)


