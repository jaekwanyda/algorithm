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
#아코테 정렬 연습 4
#N,K입력 받기
n,k=map(int,input().split())
#A,B 배열 입력받기
A=list(map(int,input().split())) #[]를 사용해서 생성하면 오류 발생 =>왜일까?=> 예상 map이 처리가 안되고 남아있는듯?
B=list(map(int,input().split()))

#아이디어: A,B를 정렬 후에 A의 제일 작은 값과 B의 제일 큰 값을 바꾼다. 
#만약 A의 제일 작은 값이 B의 제일 큰 값보다 큰 경우 멈춘다.
A=sorted(A)
B=sorted(B,reverse=True)
for i in range(k):
    if A[i]>B[i]:
        break
    A[i],B[i]=B[i],A[i]

print(sum(A))
# -


