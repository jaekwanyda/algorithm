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
#이코테 실전 31
#아이디어: 앞에 열에서 가장 최고의 금광 채굴 기록을 저장해 두면 다음 열에서 다시 이용(아이디어는 괜찮은데 틀림)
#=>2차원 DP테이블 만들어서 더 가독성 있게 코드 바꿔야함
#테스트 케이스 T입력받기
t=int(input())
for i in range(t):
    #n,m입력 받기
    n,m=map(int,input().split()) 
    #금의 개수 입력받기
    array=list(map(int,input().split()))
    #이전 결과의 최대 값 저장하는 리스트 생성
    d=[0]*n
    for i in range(n):
        d[i]=array[i*m]
    for i in range(1,m): #첫번째 행은 진행하지 않아도 됨 
        for j in range(n):
            #이전에 가능한 값들 중 가장 최대와 더해줌
            if j==0:
                d[j]=max(d[j]+array[i+j*m],d[j]+array[i+(j+1)*m]) #바로 이전 행과 이전 행 아래 열 값과 비교
            elif j==n-1:
                d[j]=max(d[j]+array[i+j*m],d[j]+array[i+(j-1)*m]) #바로 이전 행과 이전 행 윗 열 값과 비교
            else:
                d[j]=max(d[j]+array[i+j*m],d[j]+array[i+(j-1)*m],d[j]+array[i+(j+1)*m])
    print(max(d))
    

# -

d


