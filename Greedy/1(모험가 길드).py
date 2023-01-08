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

#이코테 기출 1
#아이디어: 가장 작은 단위의 모험가 그룹을 만들고, 그 다음 또 다시 가장 작은 단위의 모험가 그룹 만들기(1차 생각)
#새로운 아이디어: 생각은 맞는데 구현부분이 틀렸음. 잉여 모험가 수를 추가하면 해결 될듯
#모험가 수 입력
n=int(input())
#공포도 리스트
array=list(map(int,input().split()))
array=sorted(array) #공포도가 작은 순으로 정렬
sum=0 #그룹의 총합
r=0 #잉여 모험가
for i in array:
    r+=1 #잉여 모험가 1추가
    if i>=r: #그룹을 만들 수 있다면 만들기
        sum+=1
#총 시간 복잡도는 O(N) 으로 예상된다.       
print(sum)


