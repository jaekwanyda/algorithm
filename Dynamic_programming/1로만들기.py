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
#아코테 다이나믹 연습 2
#정수 X 입력받기
x=int(input())
d=[0]*30001 #최솟값들 저장
d[1]=0 #0으로 초기화 해주지 않으면 아래 for구문에서 1이 되어버린다. 
for i in range(2,30001): #최대 정수는 30000이다.
    a=[] #가능한 경우 중에서 가장 작은 수를 찾을 것이다. 공간메모리가 부족하면 아래 구문에서 각각 min을 취해줄 수도 있다.
    a.append(d[i-1]+1)
    if i%2==0:
        a.append(d[i//2]+1)
    if i%3==0:
        a.append(d[i//3]+1)
    if i%5==0:
        a.append(d[i//5]+1)
    d[i]=min(a)

print(d[x])
# -


