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
#재귀 함수로 구현해 보기
#중간점과 비교하고 경우에 따라 왼쪽이나 오른쪽 배열에서 다시 찾는 함수 구현
#주어진 array는 오름차순이라 정의
def bynary_sc(array,target,start,end):
    #종료 조건 표시
    if start>end:
        return None
    
    mid=(start+end)//2
    if array[mid]==target: #찾으면 그 위치의 index 출력
        return mid
    elif array[mid]<target:#오른쪽 배열에 있을 때
        return bynary_sc(array,target,mid+1,end)
    else:
        return bynary_sc(array,target,start,mid-1)
    
#n(원소의 갯수)과 target입력받기
n,target=map(int,input().split())
#array 입력받기
array=list(map(int,input().split()))

result=bynary_sc(array,target,0,len(array))

if result==None:
    print('원소가 존재하지 않습니다,')
else:
    print(result+1) # 0번 인덱스를 첫번째 요소로 여기기 때문
# -


