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
array=[5,7,9,0,3,1,6,2,4,8]

#제일 왼쪽에 있는 것을 기준으로 하는 퀵정렬
def quick_sort(array,start,end):
    if start>=end:#원소가 1개일 경우 종료
        return
    pivot=start #기준은 제일 왼쪽의 수
    left=start+1
    right=end
    #왼쪽에서부터 기준보다 큰것 찾기
    while left<=right:#왼쪽에서 찾은 수와 오른쪽에서 찾은 수가 엇갈릴 때까지 반복
        while left<=end and array[left]<=array[pivot]:
            left+=1
        while right>=left and array[right]>=array[pivot]:
            right-=1
        if right<left: #둘이 엇갈렸을 경우
            array[pivot],array[right]=array[right],array[pivot]
        else:
            array[left],array[right]=array[right],array[left]
    #작은 덩어리들도 추가적으로 해주기
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)
    
quick_sort(array,0,len(array)-1)
print(array)
# -

#좀 더 느리지만 직관적인 코드
array=[5,7,9,0,3,1,6,2,4,8]
def quick_sort(array):
    if len(array)<=1: # 원소가 하나라면 종료
        return array
    pivot=array[0]
    tail=array[1:] 
    #단순히 pivot보다 작은 값을 left_side에 큰 값을 right_side에 정리
    left_side=[x for x in tail if x<=pivot]
    right_side=[x for x in tail if x>pivot]
    
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)
print(quick_sort(array))


