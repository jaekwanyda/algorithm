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
#이코테 실전 27
#아이디어: 원하는 원소의 처음값과 끝값을 찾을 수 있으면 해결된다. 이진탐색을 이용해보자
#파이썬 라이브러리의 bisect 사용 가능
#수열의 크기 N과 원소 x입력받기
n,x=map(int,input().split())
#수열 입력받기
array=list(map(int,input().split()))
x_list=[]
#이진탐색 함수
def binary_search(array,x,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    global x_list #x의 인덱스를 저장할 리스트
    #중앙값이 찾는 값보다 클때
    if array[mid]>x:
        binary_search(array,x,start,mid-1)
    #중앙값이 찾는 값보다 작을때
    elif array[mid]<x:
        binary_search(array,x,mid+1,end)
    #중앙값이 찾는 값과 일치할 때
    else:
        binary_search(array,x,start,mid-1)
        binary_search(array,x,mid+1,end)
        x_list.append(mid)
    return None

binary_search(array,x,0,len(array)-1)

if len(x_list)==0:
    print(-1)
else:
    print(len(x_list))

# -


