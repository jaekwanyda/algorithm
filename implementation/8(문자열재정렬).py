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
#이코테 기출 8
#아이디어: 문자열을 sort하는 방법과 데이터 타입을 구별하는 함수만 알면 구현 가능할 것같다.
#문자열 입력받기
array=list(input())
sum=0
a=[]
for i in array:
    try :
        sum+=int(i)
    except ValueError:
        a.append(i)
a.sort() #문자열 정렬
a=a+[sum]

for i in a:
    print(i,end='')
# -


