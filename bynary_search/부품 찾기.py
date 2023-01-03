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
#아코테 이진탐색 연습 2
#순서가 오름차순으로 정렬된 배열 이진탐색
def by_sc(array,target,start,end):
    if start>end:
        return print('no',end=' ')
    mid=(start+end)//2
    if array[mid]==target:
        return print('yes',end=' ')
    elif array[mid]<target: #오른쪽 덩어리
        return by_sc(array,target,mid+1,end)
    else :
        return by_sc(array,target,start,mid-1)
    
#갖고있는 부품 갯수 n 입력받기
n=int(input())
#부품 배열 입력받기
array=list(map(int,input().split()))
array=sorted(array) #오름차순 정렬
#찾는 부품 갯수 m입력받기
m=int(input())
#찾는 부품 배열 입력받기
find_array=list(map(int,input().split()))
for i in find_array:
    by_sc(array,i,0,len(array))
# -


