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

#이코테 실전 24(백준 18310)
#아이디어1: 각 위치별 가장 거리가 작은 값을 찾는 것이다.계수 정렬 이용! => 시간 초과
#n입력받기
n=int(input())
#집 위치 입력받기
array=list(map(int,input().split()))
#거리 구하는 함수
def distance(array,location): #location: 안테나의 위치
    sum=0
    for i in array:
        sum+=abs(i-location)
    return sum
d=[]#거리를 저장하는 리스트
for i in range(1,max(array)+1): #최댓값 이후로는 무조건 늘기만 하니까.시간복잡도 O(10^10) 예상=> 여기서 시간 초과 생김
    d.append(distance(array,i))
#최솟값 구하기
min_distance=min(d)
min_list=[]
for i,j in enumerate(d):
    if j==min_distance:
        print(i+1)
        break
        

# +
#아이디어2: 이 문제의 함수는 절댓값 함수로 감소하다 증가하는 형태일 것이다.
#이 때 이 함수는 정확히 median에서 최솟값을 갖는다.

#n입력받기
n=int(input())
#집 위치 입력받기
array=list(map(int,input().split()))
array.sort()
a=0 
if len(array)%2==0: #짝수일 경우 median
    a=array[len(array)//2-1]
else:
    a=array[len(array)//2]
    
print(a)

# -


