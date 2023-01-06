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
#아코테 이진탐색 연습 3
#아이디어: [0,max(떡 길이)] 의 범위를 이용해 이진탐색을 이용해보자 
#최대 길이는 10억이기 때문에 이진탐색을 이용하면 해결할 수 있을거라 예상된다..
#특정한 값을 찾기 보다, 특정 길이를 넣었을 때 가능한 값 중 가장 최댓값을 찾고싶다.
#떡을 잘랐을 때 잘린 떡의 총합을 구하는 함수
def cut_cake(array,length):
    b=0
    for i in range(len(array)):
        a=array[i]-length
        if a<0:
            a=0
        b+=a
    return b

#이진 탐색 함수
def by_sc(array,target,start,end):
    if start>end:#이 문제에서는 불가능한 경우는 없다고 했기 때문에 사실 필요 없음. 혹시나 하는 경우를 위해 만듬
        return start-1 
    mid=(start+end)//2
    if cut_cake(array,mid)<target: # 중간값으로 불가능하면 왼쪽 배열 확인
        return by_sc(array,target,start,mid-1)
    else :
        return by_sc(array,target,mid+1,end)
    
#떡의 개수(N) 과 원하는 떡의 길이 (target)입력받기
n,target=map(int,input().split())
#각 떡의 높이 입력받기
array=list(map(int,input().split()))
array=sorted(array)

result=by_sc(array,target,0,array[len(array)-1])

print(result)

# +
#반복문으로 해결하기!! (더 간걸함, 몰랐음)
#입력받기는 똑같다.
#떡의 개수(N) 과 원하는 떡의 길이 (target)입력받기
n,target=map(int,input().split())
#각 떡의 높이 입력받기
array=list(map(int,input().split()))
array=sorted(array)#사실 정렬은 필요없다. 최댓값을 구하기 위해서 사용했는데 그냥 max(array)로도 해결
start=0
end=array[len(array)-1]

#이진 탐색 구현
result=0
while(start<=end):
    mid=(start+end)//2
    total=0
    #떡길이 총합 구하기
    for x in array:
        if x>mid:
            total+=x-mid
    if total<target:#자른 떡의 양이 더 작을 때엔 더 잘라야 한다=> 왼쪽으로 이동
        end=mid-1
    else:#더 많을 때에는 덜 잘라야 한다 => 오른쪽으로 이동
        start=mid+1
        #최대한 덜 잘라야하니까 가능할 때 result로 저장
        result=mid

print(result)min()
# -


