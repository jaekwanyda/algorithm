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
#아코테 정렬 연습 3
#N 입력받기
n= int(input())

#이름과 성적 입력받기
array=[]
for i in range(n):
    input_data=input().split()
    array.append([input_data[0],int(input_data[1])])

array=sorted(array,key=lambda x:x[1]) #key를 이용한 정렬(몰랐던 점!)

for student in array:
    print(student[0], end=' ')
# -


